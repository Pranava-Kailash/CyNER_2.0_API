from fastapi import APIRouter, Depends
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from sqlalchemy.orm import Session
from database import get_db
import schemas, model as db_model

router = APIRouter()

# Load the model and tokenizer
path_to_checkpoint = 'PranavaKailash/CyNER-2.0-DeBERTa-v3-base'
tokenizer = AutoTokenizer.from_pretrained(path_to_checkpoint, use_fast=True, max_length=768)
model = AutoModelForTokenClassification.from_pretrained(path_to_checkpoint)
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

@router.post("/ner", response_model=schemas.NERResponse)
async def perform_ner(request: schemas.NERRequest, db: Session = Depends(get_db)):
    entities = ner_pipeline(request.text)
    
    entities_dict = {}
    for entity in entities:
        entity_type = entity['entity']
        if entity_type not in entities_dict:
            entities_dict[entity_type] = []
        entities_dict[entity_type].append({
            "entity": entity['entity'],
            "score": entity['score'],
            "index": entity['index'],
            "word": entity['word'],
            "start": entity['start'],
            "end": entity['end']
        })

    def tag_sentence(sentence, entities_dict):
        all_entities = sorted(
            [(e['start'], e['end'], e['entity'], e['word']) for ents in entities_dict.values() for e in ents],
            key=lambda x: x[0]
        )

        merged_entities = []
        current_entity = None

        for start, end, entity_type, word in all_entities:
            if current_entity is None:
                current_entity = [start, end, entity_type, word]
            else:
                # Check if this is the continuation of the current entity
                if start == current_entity[1] and entity_type == current_entity[2] and entity_type.startswith('I-'):
                    current_entity[1] = end
                    current_entity[3] += word.replace('▁', ' ') 
                else:
                    # Save the current entity and start a new one
                    merged_entities.append(tuple(current_entity))
                    current_entity = [start, end, entity_type, word]

        # Don't forget to add the last entity
        if current_entity:
            merged_entities.append(tuple(current_entity))

        # Build the tagged sentence
        tagged_sentence = ""
        last_idx = 0

        for start, end, entity_type, _ in merged_entities:
            tagged_sentence += sentence[last_idx:start]
            entity_tag = entity_type.replace('I-', 'B-')
            tagged_sentence += f"<{entity_tag}>{sentence[start:end]}</{entity_tag}>"
            last_idx = end

        tagged_sentence += sentence[last_idx:]

        return tagged_sentence

    # Generate the tagged sentence
    tagged_sentence_str = tag_sentence(request.text, entities_dict)

    # Save the data to the database (if needed)
    db_entry = db_model.NERData(input_text=request.text, output_entities=str(entities_dict), tagged_sentence=tagged_sentence_str)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

    # Return the entities and the tagged sentence
    return {"entities": entities_dict, "tagged_sentence": tagged_sentence_str}




