import React from "react";
const Student = ({ name, words }) => (
  <div>
    Name: {name}
    <br />
    Words:
    <ul>
      {words.map((word, i) => (
        <li key={i}>{word}</li>
      ))}
    </ul>
  </div>
);

export default Student;

// components that only handle what is shown on the page
