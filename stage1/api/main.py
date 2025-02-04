from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from number import ClassifyNumber


app = FastAPI()
classifier = ClassifyNumber()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://hng-backend-track.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
def api():
    return {"message": "Welcome Home"}


@app.get("/api/classify-number")
async def clasify_number(number: int = Query(..., description="Number to classify")):
    """public api to display number properties"""
    try:
        number = int(number)
        is_prime = classifier.is_prime(number)
        is_perfect = classifier.is_perfect(number)
        digit_sum = classifier.digit_sum(number)
        fun_fact = await classifier.fun_fact(number)
        number_check = classifier.is_armstrong(number)
        numb_check = classifier.is_odd_or_even(number)
        properties = []
        if number_check and numb_check == "odd":
            properties = ["armstrong", "odd"]
        elif number_check and numb_check == "even":
            properties = ["armstrong", "even"]
        elif numb_check == "odd":
            properties = ["odd"]
        elif numb_check == "even":
            properties = ["even"]
        return {
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }
    except Exception as e:
        return {
            "number": "alphabet",
            "error": True
        }
