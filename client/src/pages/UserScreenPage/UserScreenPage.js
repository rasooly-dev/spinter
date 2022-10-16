import React, { useEffect } from "react";
import './UserScreenPage.css';
function UserScreenPage() {
    const handleSubmit = (event) => {
        //make a post request 
        
    };
    return (
    <div id="speechContainer">
    <h1> Please Upload new File</h1>
    {/* <form method="post" encType="multipart/form-data">
        <input type="file" name="file" accept="mp3"></input>
        <br></br>
        <input type="submit" value="Transcribe" />
    </form> */}
    <form onSubmit={handleSubmit} encType="multipart/form-data">
        <input type="file" name="file" accept="mp3"></input>
        <br></br>
        <input type="submit" value="Transcribe" />
    </form>
    </div>
    );
}

export default UserScreenPage;
