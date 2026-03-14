from starlette.responses import RedirectResponse
from fastapi.responses import Response,FileResponse
from fastapi import FastAPI, File,UploadFile,Request
from fastapi.middleware.cors import CORSMiddleware
from src.pipeline.trainingPipeline import Training
from src.pipeline.batchPredictionPipeline import PredictionPipeline
from src.exception import NetworkSecurityException
from uvicorn import run as app_run
import sys
import os
import pandas as pd

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train():
    try:
        train=Training()
        train.start_training_pipeline()
        return Response("Training successful",status_code=200)
    except Exception as e:
        raise NetworkSecurityException(e,sys)

@app.post("/predict")
async def predict(request:Request,file:UploadFile=File(...)):
    try:
        df=pd.read_csv(file.file)
        prediction=PredictionPipeline()
        y_pred=prediction.start_prediction_pipeline(df)
        df['prediction_column']=y_pred
        df["prediction_column"].replace(0.0,-1,inplace=True)
        os.makedirs("prediction",exist_ok=True)
        df.to_csv("prediction/output.csv",index=False,header=True)
        # return Response("Prediction successful",status_code=200)
        return FileResponse(
            path="prediction/output.csv",
            media_type="text/csv",
            filename="output.csv"
        )
    except Exception as e:
        raise NetworkSecurityException(e,sys)

if __name__=="__main__":
    app_run(app,host="0.0.0.0",port=8080)