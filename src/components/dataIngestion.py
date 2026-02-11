import os
import sys
from sklearn.model_selection import train_test_split
from src.entity.config_entity import DataIngestionConfig
from dotenv import load_dotenv
import pymongo
import pandas as pd
import numpy as np
from src.exception import NetworkSecurityException
from src.entity.artifact_entity import DataIngestionArtifact


load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
    
    def load_data(self):
        try:
            db=self.data_ingestion_config.database
            collection=self.data_ingestion_config.collection
            mongo_client=pymongo.MongoClient(MONGO_URI)[db][collection]
            records=pd.DataFrame(list(mongo_client.find()))
            if records.empty:
                raise NetworkSecurityException("No records Found",sys)
            if "_id" in records.columns.to_list():
                records.drop(columns=["_id"],axis=1,inplace=True)
            records.replace({"na":np.nan},inplace=True)
            return records
        except Exception as e:
            NetworkSecurityException(e,sys)
    

    def  train_test_spilt(self,dataFrame:pd.DataFrame):
        try:
            feature_file_path=self.data_ingestion_config.featured_file_path
            train_file_path=self.data_ingestion_config.train_file_path
            test_file_path=self.data_ingestion_config.test_file_path
            train_ratio=self.data_ingestion_config.train_test_ratio
            train_data,test_data=train_test_split(dataFrame,train_size=train_ratio,random_state=6)

            directry_name=os.path.dirname(feature_file_path)
            os.makedirs(directry_name,exist_ok=True)

            dataFrame.to_csv(feature_file_path,index=False,header=True)
            train_data.to_csv(train_file_path,index=False,header=True)
            test_data.to_csv(test_file_path,index=False,header=True)
            return
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def intialize_data_ingestion(self):
        try:
            records=self.load_data()
            self.train_test_spilt(records)
            print(len(records))
            return DataIngestionArtifact(self.data_ingestion_config.train_file_path,self.data_ingestion_config.test_file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
