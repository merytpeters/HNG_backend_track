from fastapi import FastAPI
from datetime import datetime



app = FastAPI()


@app.get("/userinfo")
def userInfo(
    email: str = "merytpeters@gmail.com",
    githuburl: str = "https://github.com/merytpeters/HNG_backend_track"
):
    """public api to display required info"""
    return {
        "email":   email,
        "current_datetime":   datetime.now().isoformat(timespec='seconds') + "Z",
        "github_url":   githuburl
    }

