from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


def max1(numbers: List[float]) -> float:
    return max(numbers)


def min1(numbers: List[float]) -> float:
    return min(numbers)


def avg(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)


def std_dev(numbers: List[float]) -> float:
    average = avg(numbers)
    variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5


class NumberInput(BaseModel):
    numbers: List[float]


@app.get("/statistics_query")
async def statistics_query(numbers: List[float]):
    maximum = max1(numbers)
    minimum = min1(numbers)
    average = avg(numbers)
    standard_deviation = std_dev(numbers)
    return {
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "standard_deviation": standard_deviation
    }


@app.get("/statistics_path/{numbers}")
async def statistics_path(numbers: str):
    number_list = [float(num) for num in numbers.split(",")]
    maximum = max1(number_list)
    minimum = min1(number_list)
    average = avg(number_list)
    standard_deviation = std_dev(number_list)
    return {
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "standard_deviation": standard_deviation
    }


@app.post("/statistics_body")
async def statistics_body(input: NumberInput):
    numbers = input.numbers
    maximum = max1(numbers)
    minimum = min1(numbers)
    average = avg(numbers)
    standard_deviation = std_dev(numbers)
    return {
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "standard_deviation": standard_deviation
    }
