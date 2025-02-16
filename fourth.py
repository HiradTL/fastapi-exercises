from fastapi import FastAPI

app = FastAPI()

def numbers(number):
    num = str(number)
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

def find_numbers():
    results = []
    for number in range(100, 1000):
        if numbers(number):
            results.append(number)
    return results

@app.get("/result")
async def calculate_path():
    numbers = find_numbers()
    return {"numbers": numbers}