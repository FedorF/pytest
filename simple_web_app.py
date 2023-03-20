import os
import time

import uvicorn
from fastapi import FastAPI

from dto.data_models import Customer, ChurnResponse


app = FastAPI()


@app.on_event("startup")
def load_model():
    """Loading fake model.
    """
    time.sleep(2)


@app.get("/")
def main():
    return {"info": "Pytest demo."}


@app.post("/predict/", response_model=ChurnResponse)
def predict(request: Customer):
    if request.age >= 50:
        return ChurnResponse(score=0.5)
    return ChurnResponse(score=0.1)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
