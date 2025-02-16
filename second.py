from fastapi import FastAPI

app = FastAPI()


def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result


@app.get("/result")
async def calculate_path():
    result = 0
    sign = 1
    makharj_aval = 11
    for i in range(14):
        soorat = factorial(3 + 2 * i)
        makhraj = makharj_aval - i
        if makhraj == 0:
            kasr = 0
        else:
            kasr = soorat / makhraj
        result += sign * kasr
        sign = -sign
    return {"result": result}
