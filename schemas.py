from pydantic import BaseModel
from typing import Dict, List

class NERRequest(BaseModel):
    text: str

class Entity(BaseModel):
    entity: str
    score: float
    index: int
    word: str
    start: int
    end: int

class NERResponse(BaseModel):
    entities: Dict[str, List[Entity]]
    tagged_sentence: str 
