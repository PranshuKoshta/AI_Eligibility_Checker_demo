from scoring import (
    calculate_ausbildung_score,
    calculate_healthcare_score
)


def evaluate_candidate(answers):

    ausbildung = calculate_ausbildung_score(answers)

    healthcare = calculate_healthcare_score(answers)

    # ----------------------------
    # Determine recommendation
    # ----------------------------

    if healthcare["score"] >= ausbildung["score"]:

        recommended_program = (
            "German Healthcare Program"
        )

        final_score = healthcare["score"]

        strengths = healthcare["strengths"]

        weaknesses = healthcare["weaknesses"]

    else:

        recommended_program = (
            "Germany Skilled Career Pathway"
        )

        final_score = ausbildung["score"]

        strengths = ausbildung["strengths"]

        weaknesses = ausbildung["weaknesses"]

    # ----------------------------
    # Profile fit status
    # ----------------------------

    if final_score >= 75:
        profile_fit = "Strong Candidate"

    elif final_score >= 55:
        profile_fit = "Potential / Pipeline Candidate"

    else:
        profile_fit = "Needs Improvement"

    print("\n===== FINAL EVALUATION =====")

    print("Ausbildung Score:", ausbildung["score"])

    print("Healthcare Score:", healthcare["score"])

    print("Recommended Program:", recommended_program)

    print("============================\n")

    return {
        "recommended_program":
            recommended_program,

        "profile_fit_status":
            profile_fit,

        "ausbildung_score":
            ausbildung["score"],

        "healthcare_score":
            healthcare["score"],

        "strengths":
            strengths,

        "weaknesses":
            weaknesses
    }