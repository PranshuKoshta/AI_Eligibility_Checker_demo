const questions = [
  {
    id: "age",
    question: "What is your age?",
    options: [
      "18–23",
      "24–28",
      "29–32",
      "33–37",
      "38 or above"
    ]
  },

  {
    id: "education",
    question: "What is your highest completed education?",
    options: [
      "12th Pass",
      "Diploma / ITI",
      "Bachelor’s Degree",
      "B.Tech / Engineering",
      "Healthcare Degree (GNM, BSc Nursing, Physiotherapy, etc.)"
    ]
  },

  {
    id: "background",
    question: "Which field is closest to your educational or professional background?",
    options: [
      "Healthcare (Nursing, Physiotherapy, Medical, etc.)",
      "Technical / ITI / Skilled Trades",
      "IT / Engineering",
      "Business / Management / Commerce",
      "General / Non-technical"
    ]
  },

  {
    id: "experience",
    question: "How much relevant work experience do you have?",
    options: [
      "No experience",
      "Less than 6 months",
      "6 months to 1 year",
      "1–3 years",
      "More than 3 years"
    ]
  },

  {
    id: "german_level",
    question: "What is your current German language level?",
    options: [
      "No German knowledge",
      "A1",
      "A2",
      "B1",
      "B2 or above"
    ]
  },

  {
    id: "willingness",
    question: "Are you willing to learn German up to B1/B2 level if required?",
    options: [
      "Yes, fully committed",
      "Yes, but unsure about the difficulty",
      "Maybe",
      "No"
    ]
  },

  {
    id: "healthcare_license",
    question:
      "Do you have a professional healthcare certification, registration, or license?",
    options: [
      "Yes",
      "No",
      "Currently pursuing"
    ],
    conditional: {
      dependsOn: "background",
      showIf:
        "Healthcare (Nursing, Physiotherapy, Medical, etc.)"
    }
  }
];

export default questions;