from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


def f1(number):
    max_digit = max(number)
    return max_digit


def f2(number, max_digit):
    new_digit = ""
    found = False
    for i in range(len(number)):
        if number[i] == max_digit and not found:
            found = True
        else:
            new_digit += number[i]
    return new_digit


class NumberInput(BaseModel):
    number: str


@app.get("/process_query")
async def process_query(number: str):
    max_digit = f1(number)
    final_number = f2(number, max_digit)
    return {"final_number": final_number}


@app.get("/process_path/{number}")
async def process_path(number: str):
    max_digit = f1(number)
    final_number = f2(number, max_digit)
    return {"final_number": final_number}


@app.post("/process_body")
async def process_body(input: NumberInput):
    number = input.number
    max_digit = f1(number)
    final_number = f2(number, max_digit)
    return {"final_number": final_number}
