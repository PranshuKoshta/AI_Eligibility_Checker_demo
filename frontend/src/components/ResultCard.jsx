function ResultCard({ result }) {

  return (
    <div>

      <h1>Eligibility Result</h1>

      <h2>Recommended Program</h2>

      <p>{result.recommended_program}</p>

      <h2>Profile Fit Status</h2>

      <p>{result.profile_fit_status}</p>

      <h2>Scores</h2>

      <p>
        Ausbildung Score:
        {" "}
        {result.ausbildung_score}
        / 100
      </p>

      <p>
        Healthcare Score:
        {" "}
        {result.healthcare_score}
        / 100
      </p>

      <h2>Strengths</h2>

      <ul>
        {result.strengths.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>

      <h2>Weaknesses</h2>

      <ul>
        {result.weaknesses.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>

    </div>
  );
}

export default ResultCard;