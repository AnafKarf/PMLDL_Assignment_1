from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()


class Input(BaseModel):
    Age: int
    Sex: str
    Height: float
    Weight: float
    Children: int
    Smoker: str


@app.post("/predict")
def predict(input_data: Input):
    age = input_data.Age / 65
    sex_to_int = {
        'male': 0,
        'female': 1
    }

    smoker_to_int = {
        'no': 0,
        'yes': 1
    }
    sex = sex_to_int[input_data.Sex]
    bmi = (input_data.Weight / ((input_data.Height / 100) ** 2)) / 40
    children = input_data.Children / 5
    smoker = smoker_to_int[input_data.Smoker]
    data = [[
        age,
        sex,
        bmi,
        children,
        smoker
    ]]

    prediction = model.predict(pd.DataFrame(data, columns=['Age', 'Sex', 'BMI', 'Children', 'Smoker']))
    return {"prediction": int(prediction[0])}