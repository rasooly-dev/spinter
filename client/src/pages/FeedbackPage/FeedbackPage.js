import React, {useState} from "react";

function FeedbackPage() {
  const handleSubmit = () => {};
  const onChangeHandler = () => {};
  const [firstMsg, setFirstMsg] = useState("");
  const [secondMsg, setSecondMsg] = useState("");
  const [thirdMsg, setThirdMsg] = useState("");
  useEffect(() => {
    //fetch api 
    setFirstMsg(api_body_1);
    setSecondMsg(api_body_2);
    setThirdMsg(api_body_3);
  });

  return (
    <div>
      <div className="card">
        <div className="card-body">{firstMsg}</div>
      </div>
      <div className="card">
        <div className="card-body">{secondMsg}</div>
      </div>
      <div className="card">
        <div className="card-body">{thirdMsg}</div>
      </div>
    </div>
  );
}

export default FeedbackPage;
