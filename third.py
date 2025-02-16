from fastapi import FastAPI

app = FastAPI()


def find_numbers():
    results = []
    for number in range(1000, 10000):
        num = str(number)
        first_two_sum = int(num[0]) + int(num[1])
        last_two_product = int(num[2]) * int(num[3])
        if first_two_sum == last_two_product:
            results.append(number)
    return results


@app.get("/result")
async def calculate_path():
    numbers = find_numbers()
    return {"numbers": numbers}
