from fastapi import FastAPI

app = FastAPI()


@app.get("/even_digits")
async def even_digits(number: str):
    first_evan = True
    result = ""
    for digits in number:
        if int(digits) % 2 == 0:
            evan_digits = digits
            if not first_evan:
                result += "*"
            result += evan_digits
            first_evan = False
    return {"result": result}