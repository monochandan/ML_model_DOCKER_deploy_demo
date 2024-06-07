## create an API
from fastapi import FastAPI
import joblib
import numpy as np

## load the model
model = joblib.load('app/model.joblib')

##  for interpreting the mdoel we need the class names
class_names = np.array(['setosa', 'versicolor', 'virginica'])

## creating an app using the fastAPI
app = FastAPI()

## decorator : tels the fastAPI that functions below handle all the request coming to this path
@app.get('/')
def reed_root():
    return {'message': 'Iris model API'}


@app.post('/predict')
def predict(data:dict):
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'predicted_class': class_name}