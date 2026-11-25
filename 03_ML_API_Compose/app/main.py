
import os
from contextlib import asynccontextmanager

import psycopg
from fastapi import FastAPI
from pydantic import BaseModel

def get_connection():

    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=5432
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id SERIAL PRIMARY KEY,
                input_value FLOAT,
                prediction FLOAT
            )
        """)
    yield


app = FastAPI(lifespan= lifespan)

class PredictionInput(BaseModel):
    x: float


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: PredictionInput):

    # Placeholder prediction logic.
    # We'll replace this with an actual trained ML model later.
    prediction = 2 * data.x + 5

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO predictions (input_value, prediction)
            VALUES (%s, %s)
            """,
            (data.x, prediction)
        )

    return {
        "input": data.x,
        "prediction": prediction
    }



@app.get("/prediction")
def get_prediction():
    with get_connection() as conn:
        rows = conn.execute(
            "select id, input_value, prediction from predictions order by id"

        ).fetchall()

    return [
        {
            "id": row[0], 
            "input": row[1], 
            "prediction": row[2]
        }
        for row in rows
    ]