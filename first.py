from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/even_digits_query")
async def even_digits_query(number: str):
    first_even = True
    result = ""
    for digit in number:
        if int(digit) % 2 == 0:
            even_digit = digit
            if not first_even:
                result += "*"
            result += even_digit
            first_even = False
    return {"even_digits": result}


@app.get("/even_digits_path/{number}")
async def even_digits_path(number: str):
    first_even = True
    result = ""
    for digit in number:
        if int(digit) % 2 == 0:
            even_digit = digit
            if not first_even:
                result += "*"
            result += even_digit
            first_even = False
    return {"even_digits": result}


class NumberInput(BaseModel):
    number: str


@app.post("/even_digits_body")
async def even_digits_body(input: NumberInput):
    number = input.number
    first_even = True
    result = ""
    for digit in number:
        if int(digit) % 2 == 0:
            even_digit = digit
            if not first_even:
                result += "*"
            result += even_digit
            first_even = False
    return {"even_digits": result}
