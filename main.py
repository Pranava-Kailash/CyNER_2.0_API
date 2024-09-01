from fastapi import FastAPI
from routers import ner
from database import engine
from model import Base
import uvicorn


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ner.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
