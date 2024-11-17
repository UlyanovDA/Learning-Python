# TODO решите задачу
import json

INPUT = 'input.json'
def task() -> float:
    with open(INPUT, 'r') as f:
        data = json.load(f)

    suma = sum([i['score']*i['weight'] for i in data])
    return round(suma, ndigits=3)


print(task())
