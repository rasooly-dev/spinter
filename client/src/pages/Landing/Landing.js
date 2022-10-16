import React, { useState , setTheArray} from "react";
import "./Landing.css";
function Landing() {
  const [firstQ, setFirstQ] = useState("");
  const [secondQ, setSecondQ] = useState("");
  const [thirdQ, setThirdQ] = useState("");

  const [firstQ2, setFirstQ2] = useState("");
  const [secondQ2, setSecondQ2] = useState("");
  const [thirdQ2, setThirdQ2] = useState("");
  const [fourthQ2, setFourthQ2] = useState("");

  const [listSoftSkill, setListSoftSkill] = useState([])
  const [listTSkill, setTSkill] = useState([])

  const [isFirstForm, setFirstForm] = useState(true);

  const handleSoftSkill = (event) => {
    setListSoftSkill(listSoftSkill => [...listSoftSkill, event.target.value])
    console.log(listSoftSkill)
  }

  const handleTSkill = (event) => {
        setTSkill(listTSkill => [...listTSkill, event.target.value])
        console.log(listTSkill)
    }

  const handleChange1 = (event) => {
    setFirstQ(event.target.value);
  };
  const handleChange2 = (event) => {
    setSecondQ(event.target.value);
  };
  const handleChange3 = (event) => {
    setThirdQ(event.target.value);
  };

  const handleChange1p2 = (event) => {
    setFirstQ2(event.target.value);
  };
  const handleChange2p2 = (event) => {
    setSecondQ2(event.target.value);
  };
  const handleChange3p2 = (event) => {
    setThirdQ2(event.target.value);
  };
  const handleChange4p2 = (event) => {
    setFourthQ2(event.target.value);
  };

  const handleToggle1 = () => {
    if (!isFirstForm) {
      setFirstForm(true);
    }
  };

  const handleToggle2 = () => {
    if (isFirstForm) {
      setFirstForm(false);
    }
  };

  const handleSubmit = () => {
    //parse information into json
    if (isFirstForm) {
        //parse and send a post req to api
        //use firstQ, secondQ, thirdQ
        console.log("lmao")
    } else {
        //parse and send post req to api
        //use firstQ2, secondQ4, listTSkill, listSoftSkill
        console.log("no")
    }
  };

  return (
    <div className="grid-container">
      {/* <!--   <div className="grid-item"></div> --> */}
      <div className="center-grid">
        <h1>Splinter</h1>
      </div>
      <div className="center-grid">
        <h1>AI</h1>
      </div>
      <div className="center-grid tab1">
        {/* <!--     create a flexbox container --> */}
        <div className="grid-container">
          <div className="center-grid">
            <div id="exTab3">
              <ul className="nav nav-pills">
                <li className="active">
                  <a href="#1b" data-toggle="tab" onClick={handleToggle1}>
                    Preselect
                  </a>
                </li>
                <li>
                  <a href="#2b" data-toggle="tab" onClick={handleToggle2}>
                    Generate
                  </a>
                </li>
              </ul>

              <div className="tab-content clearfix">
                {isFirstForm ? (
                  <div className="tab-pane active" id="1b">
                    <form onSubmit={handleSubmit}>
                      <div className="form-group">
                        <label htmlFor="exampleFormControlTextarea1">
                          Question 1{" "}
                        </label>
                        <textarea
                          className="form-control"
                          id="exampleFormControlTextarea1"
                          rows="3"
                          value={firstQ}
                          onChange={handleChange1}
                          name="q1"
                        ></textarea>
                      </div>
                      <div className="form-group">
                        <label htmlFor="exampleFormControlTextarea1">
                          Question 2{" "}
                        </label>
                        <textarea
                          className="form-control"
                          id="exampleFormControlTextarea1"
                          rows="3"
                          value={secondQ}
                          onChange={handleChange2}
                          name="q2"
                        ></textarea>
                      </div>
                      <div className="form-group">
                        <label htmlFor="exampleFormControlTextarea1">
                          Question 3
                        </label>
                        <textarea
                          className="form-control lastq"
                          id="exampleFormControlTextarea1"
                          rows="3"
                          value={thirdQ}
                          onChange={handleChange3}
                          name="q3"
                        ></textarea>
                      </div>
                      <button
                        type="submit"
                        className="btn btn-success mb-2 submit-button"
                      >
                        Get Started
                      </button>
                    </form>
                  </div>
                ) : (
                //   <div className="tab-pane" id="2b">
                //     <form>
                //       <div className="form-group">
                //         <label htmlFor="exampleFormControlTextarea1">
                //           Job Title
                //         </label>
                //         <input
                //           className="form-control"
                //           type="text"
                //           placeholder="Default input"
                //           value={firstQ2}
                //           onChange={handleChange}
                //         ></input>
                //       </div>

                //       <div className="form-group">
                //         <label htmlFor="exampleFormControlTextarea1">
                //           Soft Skills
                //         </label>
                //         <input
                //           className="form-control"
                //           type="text"
                //           placeholder="Default input"
                //           value={secondQ2}
                //           onChange={handleChange}
                //         ></input>
                //       </div>
                //       <div className="form-group">
                //         <label htmlFor="exampleFormControlTextarea1">
                //           Technical Questions
                //         </label>
                //         <input
                //           className="form-control"
                //           type="text"
                //           placeholder="Default input"
                //           value={thirdQ2}
                //           onChange={handleChange}
                //         ></input>
                //       </div>
                //       <div className="form-group">
                //         <label htmlFor="exampleFormControlTextarea1">
                //           Qualifications
                //         </label>
                //         <input
                //           className="form-control"
                //           type="text"
                //           placeholder="Default input"
                //           value={fourthQ2}
                //           onChange={handleChange}
                //         ></input>
                //       </div>
                //       <button
                //         type="submit"
                //         className="btn btn-success mb-2 submit-button"
                //       >
                //         Get Started
                //       </button>
                //     </form>
                //   </div>
                <div className="tab-pane active" id="1b">
                <form onSubmit={handleSubmit}>
                  <div className="form-group">
                    <label htmlFor="exampleFormControlTextarea1">
                      Job Title{" "}
                    </label>
                    <input
                      className="form-control"
                      type="text"
                      id="exampleFormControlTextarea1"
                      rows="3"
                      value={firstQ2}
                      onChange={handleChange1p2}
                      name="jobtitle"
                    ></input>
                  </div>
                  
                  <ul>
                    {listSoftSkill.map(skill => (<li> {skill} </li>))}
                  </ul>
                  <div className="form-group">
                    <label htmlFor="exampleFormControlTextarea1">
                    Soft Skills{" "}
                    </label>
                    <input
                      className="form-control"
                      type="text"
                      id="exampleFormControlTextarea1"
                      rows="3"
                      value={secondQ2}
                      onChange={handleChange2p2}
                      name="softskills"
                    ></input>
                  </div>

                  <button
                    type="button"
                    onClick={handleSoftSkill}
                    className="btn btn-success mb-2 submit-button"
                    value={secondQ2}
                  >
                    ADD
                  </button>

                  <ul>
                    {listTSkill.map(skill => (<li> {skill} </li>))}
                  </ul>

                  <div className="form-group">
                    <label htmlFor="exampleFormControlTextarea1">
                      Technical Skills
                    </label>
                    <input
                      className="form-control"
                      type="text"
                      id="exampleFormControlTextarea1"
                      rows="3"
                      value={thirdQ2}
                      onChange={handleChange3p2}
                      name="technicalskills"
                    ></input>
                  </div>
                  <button
                    type="button"
                    onClick={handleTSkill}
                    className="btn btn-success mb-2 submit-button"
                    value={thirdQ2}
                  >
                    ADD
                  </button>
                  <div className="form-group">
                    <label htmlFor="exampleFormControlTextarea1">
                        Job Description
                    </label>
                    <input
                      className="form-control"
                      type="text"
                      id="exampleFormControlTextarea1"
                      rows="3"
                      value={fourthQ2}
                      onChange={handleChange4p2}
                      ame="jobdesc"
                    ></input>
                  </div>

                  <button
                    type="submit"
                    className="btn btn-success mb-2 submit-button"
                  >
                    Get Started
                  </button>
                </form>
              </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Landing;
