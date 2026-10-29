from fastapi import FastAPI, HTTPException
from app.split_evenly import split_evenly

app = FastAPI()


@app.get("/split-evenly")
def split_evenly_endpoint(total_amount: float, num_people: int):
    try:
        split_amounts = split_evenly(total_amount, num_people)
        return {"split_amounts": [float(amount) for amount in split_amounts]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
