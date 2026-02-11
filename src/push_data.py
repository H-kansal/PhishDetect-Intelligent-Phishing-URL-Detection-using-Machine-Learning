import os
import sys
import json
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import pymongo
from src.exception import NetworkSecurityException
from src.logger import logging

load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")
MONGO_DB=os.getenv("MONGO_DB")

class NetworkDataETL:
    def __init__(self):
        self.MONGO_URI=MONGO_URI
        self.MONGO_DB=MONGO_DB
    
    def csv_to_json(self,file_path):
        try:
            logging.info("converting csv to json")
            csv_data=pd.read_csv(file_path)
            csv_data.reset_index(drop=True,inplace=True)
            json_data=list(json.loads(csv_data.T.to_json()).values())
            logging.info("converting csv to json completed")
            return json_data
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def loads_to_mongoDB(self,json_data):
        try:
            logging.info("loading data to mongoDB")
            mongo_client=pymongo.MongoClient(self.MONGO_URI)
            mongo_db=mongo_client[self.MONGO_DB]
            mongo_collection=mongo_db["network_data"]
            mongo_collection.insert_many(json_data)
            logging.info("loading data to mongoDB completed")
            return len(json_data)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    networkdataobj=NetworkDataETL()
    json_data=networkdataobj.csv_to_json(os.path.join('NetworkData','phisingData.csv'))
    recordLen=networkdataobj.loads_to_mongoDB(json_data)

    print(recordLen)