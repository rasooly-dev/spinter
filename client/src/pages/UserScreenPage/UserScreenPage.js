import React, { useEffect ,useState} from "react";
import './UserScreenPage.css';
function UserScreenPage() {
    const [selectedFile, setSelectedFile] = useState();
    const [isSelected, setIsSelected] = useState(false);
	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsSelected(true);
	};

	const handleSubmission = () => {
        const formData = new FormData();

		formData.append('File', selectedFile);
        //fetch post request
	};
    return (
    <div id="speechContainer">
    <h1> Please Upload new File</h1>
    {/* <form method="post" encType="multipart/form-data">
        <input type="file" name="file" accept="mp3"></input>
        <br></br>
        <input type="submit" value="Transcribe" />
    </form> */}
    <form onSubmit={handleSubmission} encType="multipart/form-data">
        <input type="file" name="file" accept="mp3" onChange={changeHandler}></input>
        <br></br>
        <input type="submit" value="Transcribe" />
    </form>
    </div>
    );
}

export default UserScreenPage;
