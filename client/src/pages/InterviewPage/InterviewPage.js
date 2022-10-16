import React, {useState, useEffect} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import './InterviewPage.css';
function InterviewPage() {
    const [interviewQuestion, setInterviewQuestion] = useState("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in lacus metus. Aenean ipsum leo, varius quis orci ut, lobortis condimentum ipsum. Donec vel purus dui?")
    const [time, setTime] = useState(180)
    useEffect(() => {
        //fetch from API
        //value = fetch()
        // setInterviewQuestion(value)
        const timer = setTimeout(() => {
            // conclude the interview and navigate to the following page
          }, 180000);
          const timer2 = setTimeout(() => {
            if (time > 0) {
                setTime(time - 1)
            } 
          }, 1000);
          return () => clearTimeout(timer);
      });
  return (
    <div>
        <div className="card">
        <div className="card-body">Interview Question</div>
      </div>
      <div className="card">
        <div className="card-body question">{interviewQuestion}</div>
      </div>
      <div className="card">
        <div className="card-body">{time}</div>
      </div>
    </div>
  );
}

export default InterviewPage;
