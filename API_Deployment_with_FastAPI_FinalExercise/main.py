from typing import Union, List
# We can aise HTML exceptions with fastapi.HTTPException
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

# Data structure definition
class Data(BaseModel):
    feature_1: float
    feature_2: str

# FastAPI app: 
app = FastAPI(
    title="Exercise API",
    description="An API that demonstrates checking the values of your inputs.",
    version="1.0.0",
)

# POST method that checks the input data
@app.post("/data/")
async def ingest_data(data: Data):
    # feature_1 must be positive
    if data.feature_1 < 0:
        raise HTTPException(status_code=400, detail="feature_1 needs to be above 0.")
    # feature_2 must be larger shorter than 280
    if len(data.feature_2) > 280:
        raise HTTPException(
            status_code=400,
            detail=f"feature_2 needs to be less than 281 characters. It has {len(data.feature_2)}.",
        )
    # If everything correct, return the same input data
    return data

# To run this:
#   uvicorn main:app --reload
# To test:
#   pytest
