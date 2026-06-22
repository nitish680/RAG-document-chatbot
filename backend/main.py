from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5501",
        "http://localhost:5501"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        'message':'this is the backend of thwe project'}
@app.post("/chat")
def chat(data:dict):
    question=data["question"]
    return {
        "answer":f"you asker {question}"
    }











