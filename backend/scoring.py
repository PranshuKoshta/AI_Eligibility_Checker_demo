def calculate_ausbildung_score(answers):

    score = 0

    strengths = []

    weaknesses = []

    # -------------------------
    # AGE
    # -------------------------

    age = answers.get("age")

    if age == "18–23":
        score += 15
        strengths.append("Excellent age range for Germany pathways")

    elif age == "24–28":
        score += 10

    elif age == "29–32":
        score += 5

    else:
        score += 2
        weaknesses.append(
            "Age may reduce Ausbildung opportunities"
        )

    # -------------------------
    # EDUCATION
    # -------------------------

    education = answers.get("education")

    if education in [
        "Diploma / ITI",
        "Bachelor’s Degree"
    ]:
        score += 25

        strengths.append(
            "Strong educational qualification"
        )

    elif education == "12th Pass":
        score += 18

    elif education == "Healthcare Degree (GNM, BSc Nursing, Physiotherapy, etc.)":
        score += 20

    # -------------------------
    # BACKGROUND
    # -------------------------

    background = answers.get("background")

    if background in [
        "Technical / ITI / Skilled Trades",
        "IT / Engineering"
    ]:
        score += 15

        strengths.append(
            "Relevant technical/professional background"
        )

    elif background == "General / Non-technical":
        score += 8

    # -------------------------
    # EXPERIENCE
    # -------------------------

    experience = answers.get("experience")

    if experience in [
        "1–3 years",
        "More than 3 years"
    ]:
        score += 15

    elif experience == "6 months to 1 year":
        score += 10

    elif experience == "Less than 6 months":
        score += 5

    # -------------------------
    # GERMAN
    # -------------------------

    german = answers.get("german_level")

    willingness = answers.get("willingness")

    if german in ["B1", "B2 or above"]:
        score += 10

        strengths.append(
            "Strong German readiness"
        )

    elif german == "A2":
        score += 8

    elif german == "A1":
        score += 5

    elif willingness in [
        "Yes, fully committed",
        "Yes, but unsure about the difficulty"
    ]:
        score += 3

        strengths.append(
            "Willing to begin German learning"
        )

    else:
        weaknesses.append(
            "German learning commitment is weak"
        )

    # -------------------------
    # MOTIVATION
    # -------------------------

    if willingness == "Yes, fully committed":
        score += 20

    elif willingness == "Yes, but unsure about the difficulty":
        score += 12

    elif willingness == "Maybe":
        score += 6

    return {
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses
    }


def calculate_healthcare_score(answers):

    score = 0

    strengths = []

    weaknesses = []

    # -------------------------
    # EDUCATION
    # -------------------------

    education = answers.get("education")

    if education == "Healthcare Degree (GNM, BSc Nursing, Physiotherapy, etc.)":

        score += 30

        strengths.append(
            "Healthcare qualification strongly matches Germany healthcare pathway"
        )

    else:

        weaknesses.append(
            "Healthcare qualification missing"
        )

    # -------------------------
    # BACKGROUND
    # -------------------------

    background = answers.get("background")

    if background == "Healthcare (Nursing, Physiotherapy, Medical, etc.)":

        score += 10

        strengths.append(
            "Relevant healthcare background"
        )

    # -------------------------
    # EXPERIENCE
    # -------------------------

    experience = answers.get("experience")

    if experience in [
        "1–3 years",
        "More than 3 years"
    ]:
        score += 20

    elif experience == "6 months to 1 year":
        score += 15

    elif experience == "Less than 6 months":
        score += 8

    else:
        weaknesses.append(
            "Healthcare experience is limited"
        )

    # -------------------------
    # GERMAN
    # -------------------------

    german = answers.get("german_level")

    willingness = answers.get("willingness")

    if german == "B2 or above":
        score += 10

    elif german == "B1":
        score += 8

    elif german in ["A1", "A2"]:
        score += 5

    elif willingness in [
        "Yes, fully committed",
        "Yes, but unsure about the difficulty"
    ]:
        score += 3

        strengths.append(
            "Open to completing German training"
        )

    else:
        weaknesses.append(
            "German training commitment is weak"
        )

    # -------------------------
    # LICENSE
    # -------------------------

    license_status = answers.get(
        "healthcare_license"
    )

    if license_status == "Yes":
        score += 10

        strengths.append(
            "Professional healthcare registration available"
        )

    elif license_status == "Currently pursuing":
        score += 5

    else:
        weaknesses.append(
            "Healthcare registration/license missing"
        )

    # -------------------------
    # MOTIVATION
    # -------------------------

    if willingness == "Yes, fully committed":
        score += 15

    elif willingness == "Yes, but unsure about the difficulty":
        score += 8

    elif willingness == "Maybe":
        score += 3

    # -------------------------
    # AGE
    # -------------------------

    age = answers.get("age")

    if age in ["24–28", "29–32"]:
        score += 5

    elif age == "33–37":
        score += 3

    else:
        score += 1

    return {
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses
    }