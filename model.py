from sqlalchemy import Column, Integer,Text
from database import Base

class NERData(Base):
    __tablename__ = "ner_data"
    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(Text, nullable=False)
    output_entities = Column(Text, nullable=False)
    tagged_sentence = Column(Text, nullable=False)
