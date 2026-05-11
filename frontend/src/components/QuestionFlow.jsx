import { useState } from "react";
import questions from "../data/questions";

function QuestionFlow() {
  const [currentIndex, setCurrentIndex] = useState(0);

  const [answers, setAnswers] = useState({});

  const currentQuestion = questions[currentIndex];

  function handleAnswer(option) {
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

    setCurrentIndex(nextIndex);
  }

  if (currentIndex >= questions.length) {
    return (
      <div>
        <h2>Completed</h2>

        <pre>
          {JSON.stringify(answers, null, 2)}
        </pre>
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