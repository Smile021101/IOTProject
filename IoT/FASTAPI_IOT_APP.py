from fastapi import FastAPI
import pickle
import numpy as np
app=FastAPI()
filename='BTL_IoT_model8.sav'
model = pickle.load(open(filename, 'rb'))
@app.post("/water/Potability/predict")
def predict(ph:float,Solids:float,Turbidity:float):
    features_list = [ph,Solids,Turbidity]
    prediction = model.predict([features_list])[0]
    message=""
    if(prediction==1):
        message="Nước chất lượng tốt,bạn có thể uống!"
    else:
        message="Nước kém chất lượng,bạn cần xử lý nó trước"
    response={"Predict":int(prediction),"Message":message}
    return (response)