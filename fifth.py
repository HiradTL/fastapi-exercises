from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NumberInput(BaseModel):
    n: int


def generate_pattern(n):
    result = []
    for i in range(1, n+1):
        row = []
        for j in range(i, (i*i)+1, i):
            row.append(j)
        result.append(row)
    return result


@app.get("/pattern_query")
async def pattern_query(n: int):
    result = generate_pattern(n)
    return {"pattern": result}


@app.get("/pattern_path/{n}")
async def pattern_path(n: int):
    result = generate_pattern(n)
    return {"pattern": result}


@app.post("/pattern_body")
async def pattern_body(input: NumberInput):
    n = input.n
    result = generate_pattern(n)
    return {"pattern": result}


# warning !!
# for see the result as a pattern turn on pretty print in your Browser
