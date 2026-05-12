def evaluate_candidate(answers):

    strengths = []

    weaknesses = []

    recommended_program = None

    background = answers.get("background")

    german_level = answers.get("german_level")

    experience = answers.get("experience")

    age = answers.get("age")

    education = answers.get("education")

    willingness = answers.get("willingness")

    healthcare_license = answers.get(
        "healthcare_license"
    )

    # ----------------------------
    # AGE ANALYSIS
    # ----------------------------

    if age in ["18–23", "24–28"]:
        strengths.append(
            "Strong age profile for German programs"
        )

    elif age == "38 or above":
        weaknesses.append(
            "Age may reduce eligibility for some pathways"
        )

    # ----------------------------
    # EDUCATION ANALYSIS
    # ----------------------------

    if education in [
        "Diploma / ITI",
        "Bachelor’s Degree"
    ]:
        strengths.append(
            "Educational background aligns well with German pathways"
        )

    if education == "Healthcare Degree (GNM, BSc Nursing, Physiotherapy, etc.)":
        strengths.append(
            "Healthcare qualification is highly valuable"
        )

    # ----------------------------
    # LANGUAGE ANALYSIS
    # ----------------------------

    if german_level in ["B1", "B2 or above"]:
        strengths.append(
            "Strong German language readiness"
        )

    elif german_level == "No German knowledge":
        weaknesses.append(
            "German language preparation is required"
        )

    # ----------------------------
    # WILLINGNESS
    # ----------------------------

    if willingness == "No":
        weaknesses.append(
            "Lack of willingness to learn German may impact eligibility"
        )

    # ----------------------------
    # HEALTHCARE PATHWAY
    # ----------------------------

    if background == "Healthcare (Nursing, Physiotherapy, Medical, etc.)":

        if (
            experience in [
                "6 months to 1 year",
                "1–3 years",
                "More than 3 years"
            ]
            and healthcare_license in [
                "Yes",
                "Currently pursuing"
            ]
        ):

            recommended_program = (
                "German Healthcare Program"
            )

            strengths.append(
                "Healthcare experience improves program fit"
            )

        else:

            weaknesses.append(
                "Healthcare pathway typically requires relevant experience and certification"
            )

    # ----------------------------
    # AUSBILDUNG PATHWAY
    # ----------------------------

    if not recommended_program:

        recommended_program = "Germany Ausbildung"

        strengths.append(
            "Candidate may qualify for Ausbildung opportunities"
        )

    return {
        "recommended_program": recommended_program,
        "strengths": strengths,
        "weaknesses": weaknesses
    }