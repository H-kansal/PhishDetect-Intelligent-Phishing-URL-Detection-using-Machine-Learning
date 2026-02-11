import os
import sys
import pandas as pd
import numpy as np
from src.exception import NetworkSecurityException
from src.logger import logging
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from src.utils.file_utils_functions import read_yaml_file,write_yaml_file
from src.constants import training
from scipy.stats import ks_2samp


YAML_FILE_PATH=os.path.join('schema','schema.yaml')

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact):
        self.data_ingestion_artifact=data_ingestion_artifact
        self.data_validation_config=DataValidationConfig()
        self._schema_config=read_yaml_file(YAML_FILE_PATH)
    @staticmethod
    def read_file(path:str):
        if not path:
            return 
        df=pd.read_csv(path)
        return df

    def check_columns_count(self,df:pd.DataFrame):
        try:
            columnsCount=columnsCount = len(self._schema_config["columns"])
            print(f"column in Yaml file:{columnsCount}")
            print(f"column in dataframe:{len(df.columns)}")
            if(len(df.columns)==columnsCount):
                return True
            return False
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def detect_dataset_drift(self,basic_df,current_df,threshold=0.03):
        try:
            status=True
            records={}
            for column in basic_df.columns:
                df1=basic_df[column]
                df2=current_df[column]
                ks_score=ks_2samp(df1,df2)
                if ks_score.pvalue<threshold:
                    is_found=True
                    status=False
                else:
                    is_found=False
                records.update({column:{
                    "score":ks_score.pvalue,
                    "status":is_found
                }})

                drift_file_path=self.data_validation_config.drift_file_path
                drift_dir=os.path.dirname(drift_file_path)
                os.makedirs(drift_dir,exist_ok=True)
            write_yaml_file(drift_file_path,records)
            return status
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def intialize_validation_data(self):
        try:
            df1=DataValidation.read_file(self.data_validation_config.invalid_train_file_path)
            df2=DataValidation.read_file(self.data_validation_config.invalid_test_file_path)
            print(f"length of df1:{len(df1)} and length of df2:{len(df2)}")
            if not self.check_columns_count(df1):
                raise NetworkSecurityException("column count is not matching",sys)
            if not self.check_columns_count(df2):
                raise NetworkSecurityException("column count is not matching",sys)
            
            status=self.detect_dataset_drift(df1,df2)
            print("drift detect answer",status)
            valid_data_dir=os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(valid_data_dir,exist_ok=True)

            df1.to_csv(self.data_validation_config.valid_train_file_path,index=False,header=True)
            df2.to_csv(self.data_validation_config.valid_test_file_path,index=False,header=True)

            return DataValidationArtifact(
                status=status,
                valid_train_data_path=self.data_validation_config.valid_train_file_path,
                valid_test_data_path=self.data_validation_config.valid_test_file_path,
                drift_file_path=self.data_validation_config.drift_file_path
            )
        except Exception as e:
            raise NetworkSecurityException(e,sys)
