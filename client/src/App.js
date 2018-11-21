import React, { Component } from "react";
import Student from "./components/Student";
// import StudentForm from "./components/StudentForm";
import "./App.css";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    const students = this.getStudentList();
    this.state = { students };
    this.addStudent = this.addStudent.bind(this);
    this.addWordToStudents = this.addWordToStudents.bind(this);
  }

  dummyStudentList = [
    // dummy starting list for now until setting backend
    { name: "Jaayden", words: ["you", "the"] },
    { name: "Selena", words: ["can", "and"] }
  ];

  getStudentList() {
    // future call to server
    return this.dummyStudentList;
  }

  addStudent(event) {
    event.preventDefault();
    const newStudent = {
      name: this.nameInput.value,
      words: []
    };

    this.setState(prevState => ({
      students: [...prevState.students, newStudent]
    }));
  }

  addWordToStudents(event) {
    event.preventDefault();
    const word = this.wordInput.value;
    const students = this.state.students.slice();
    for (let i = 0; i < students.length; i++) {
      students[i].words.push(word);
    }
    const newState = Object.assign(this.state, { students });
    this.setState(newState);
  }

  render() {
    return (
      <div>
        <h2>Students</h2>
        <div>
          {this.state.students.map((student, i) => (
            <Student key={i} name={student.name} words={student.words} />
          ))}
        </div>

        <form onSubmit={this.addStudent}>
          Add New Student
          <input
            id="nameForm"
            type="text"
            ref={nameInput => (this.nameInput = nameInput)}
          />
          <input type="submit" />
        </form>

        <form onSubmit={this.addWordToStudents}>
          Add New Word to All Students
          <input type="text" ref={wordInput => (this.wordInput = wordInput)} />
          <input type="submit" />
        </form>
      </div>
    );
  }
}

export default App;
// Components that only handle logic, components that only handle what is shown on the page

// Questions
// Designing tables/database using react/redux. Do we have to/should we be using redux?
// I want to work on stuff over thanksgiving break since I have no school all week and no plans.
// What would be the highest leverage thing to work on?
// Is it a good idea to write front end code in react for adding students and words before I design
// tables and databases?
