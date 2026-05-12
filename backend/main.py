from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rules import evaluate_candidate
from prompt_builder import build_summary_prompt
from gemini_client import generate_ai_summary
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

@app.post("/score")
def score(data: dict):

    result = evaluate_candidate(data)

    return {
        "recommended_program":
            result["recommended_program"],

        "profile_fit_status":
            result["profile_fit_status"],

        "ausbildung_score":
            result["ausbildung_score"],

        "healthcare_score":
            result["healthcare_score"],

        "strengths":
            result["strengths"],

        "weaknesses":
            result["weaknesses"]
    }

@app.post("/evaluate")
def evaluate(data: dict):

    print("Received data:", data)

    result = evaluate_candidate(data)

    prompt = build_summary_prompt(result)

    ai_summary = generate_ai_summary(prompt)

    result["ai_summary"] = ai_summary

    return result