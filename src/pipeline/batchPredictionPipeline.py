from src.exception import NetworkSecurityException
import sys
import os
from src.utils.file_utils_functions import load_object
from src.cloud.S3_Syncer import S3_Sync

class PredictionPipeline:
    def __init__(self):
        self.PREPROCESSOR_PATH=os.path.join('artifact','tranformationData','transformer_file.pkl')
        self.MODEL_PATH=os.path.join('artifact','model_training','model.pkl')


    def load_preprocessor(self):
        try:
            preprocessor=load_object(self.PREPROCESSOR_PATH)
            return preprocessor
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def load_model(self):
        try:
            model=load_object(self.MODEL_PATH)
            return model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_prediction_pipeline(self,df):
        try:
            preprocessor=self.load_preprocessor()
            model=self.load_model()
            df=preprocessor.transform(df)
            return model.predict(df)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    