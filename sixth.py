from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


def statics_needed(numbers: List[float]):
    maximum = max(numbers)
    minimum = min(numbers)
    avg = sum(numbers) / len(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    std_dev = variance ** 0.5
    return maximum, minimum, avg, std_dev


class NumberInput(BaseModel):
    numbers: List[float]


@app.get("/statistics_query")
async def statistics_query(numbers: List[float]):
    maximum, minimum, avg, std_dev = statics_needed(numbers)
    return {
        "maximum": maximum,
        "minimum": minimum,
        "average": avg,
        "standard_deviation": std_dev
    }


@app.get("/statistics_path/{numbers}")
async def statistics_path(numbers: List[float]):
    maximum, minimum, avg, std_dev = statics_needed(numbers)
    return {
        "maximum": maximum,
        "minimum": minimum,
        "average": avg,
        "standard_deviation": std_dev
    }


@app.post("/statistics_body")
async def statistics_body(input: NumberInput):
    maximum, minimum, avg, std_dev = statics_needed(input.numbers)
    return {
        "maximum": maximum,
        "minimum": minimum,
        "average": avg,
        "standard_deviation": std_dev
    }
