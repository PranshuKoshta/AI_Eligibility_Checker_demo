import { useState } from "react";
import questions from "../data/questions";
import ResultCard from "./ResultCard";
import { evaluateAnswers } from "../services/api";

function QuestionFlow() {

  const [currentIndex, setCurrentIndex] = useState(0);

  const [answers, setAnswers] = useState({});

  const [result, setResult] = useState(null);

  const [liveScores, setLiveScores] = useState({
    ausbildung_score: 0,
    healthcare_score: 0
  });

  const [loading, setLoading] = useState(false);

  const currentQuestion = questions[currentIndex];

  async function handleAnswer(option) {

    const updatedAnswers = {
      ...answers,
      [currentQuestion.id]: option
    };

    setAnswers(updatedAnswers);

    try {

    const liveResult =
      await evaluateAnswers(updatedAnswers);

    setLiveScores({
      ausbildung_score:
        liveResult.ausbildung_score,

      healthcare_score:
        liveResult.healthcare_score
    });

  } catch (error) {

    console.error(error);
  }

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
    return <ResultCard result={result} />;
  }

  return (
    <div>

      <h3>Live Eligibility Scores</h3>

        <p>
          Ausbildung:
          {" "}
          {liveScores.ausbildung_score}
          / 100
        </p>

        <p>
          Healthcare:
          {" "}
          {liveScores.healthcare_score}
          / 100
        </p>

        <hr />

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