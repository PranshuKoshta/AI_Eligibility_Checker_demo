from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rules import evaluate_candidate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "backend working"}

@app.post("/evaluate")
def evaluate(data: dict):

    print("Received data:", data)

    result = evaluate_candidate(data)

    return result