import { useState } from "react";
import questions from "../data/questions";
import { evaluateAnswers } from "../services/api";

function QuestionFlow() {

  const [currentIndex, setCurrentIndex] = useState(0);

  const [answers, setAnswers] = useState({});

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const currentQuestion = questions[currentIndex];

  async function handleAnswer(option) {

    const updatedAnswers = {
      ...answers,
      [currentQuestion.id]: option
    };

    setAnswers(updatedAnswers);

    let nextIndex = currentIndex + 1;

    while (nextIndex < questions.length) {

      const nextQuestion = questions[nextIndex];

      if (!nextQuestion.conditional) {
        break;
      }

      const dependencyAnswer =
        updatedAnswers[nextQuestion.conditional.dependsOn];

      if (
        dependencyAnswer === nextQuestion.conditional.showIf
      ) {
        break;
      }

      nextIndex++;
    }

    if (nextIndex >= questions.length) {

      setLoading(true);

      try {

        const backendResult =
          await evaluateAnswers(updatedAnswers);

        setResult(backendResult);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);
      }

    } else {

      setCurrentIndex(nextIndex);
    }
  }

  if (loading) {
    return <h2>Evaluating eligibility...</h2>;
  }

  if (result) {
    return (
      <div>
        <h2>Recommended Program</h2>

        <p>{result.recommended_program}</p>

        <h3>Strengths</h3>

        <ul>
          {result.strengths.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>

        <h3>Weaknesses</h3>

        <ul>
          {result.weaknesses.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
    );
  }

  return (
    <div>

      <h2>{currentQuestion.question}</h2>

      {currentQuestion.options.map((option) => (

        <button
          key={option}
          onClick={() => handleAnswer(option)}
          style={{
            display: "block",
            margin: "10px 0",
            padding: "12px",
            width: "300px",
            cursor: "pointer"
          }}
        >
          {option}
        </button>

      ))}

    </div>
  );
}

export default QuestionFlow;