import os
import sys
import pandas as pd
import numpy as np
from src.exception import NetworkSecurityException
from src.logger import logging
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataValidationArtifact
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from src.constants import training
from sklearn.model_selection import train_test_split
from src.utils.file_utils_functions import np_array_save,save_object
from src.entity.artifact_entity import DataTranformationArtifact

TARGET_FEATURE=training.TARGET_FEATURE
IMPUTER_PARAMS=training.IMPUTER_PARAMS


class DataTransformation:
    def __init__(self,dataValidationArtifact:DataValidationArtifact):
        self.dataValidationArtifact=dataValidationArtifact
        self.dataTransformation=DataTransformationConfig()

    @staticmethod
    def read_file(path:str):
        try:
            return pd.read_csv(path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def get_transformer(self):
        try:
            imputer=KNNImputer(**IMPUTER_PARAMS)
            processor=Pipeline([
                ("imputer",imputer)
            ])

            return processor
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def intialize_tranformation(self):

        df1=DataTransformation.read_file(self.dataValidationArtifact.valid_train_data_path)
        df2=DataTransformation.read_file(self.dataValidationArtifact.valid_test_data_path)

        train_input_feature=df1.drop(['Result'],axis=1)
        train_output_feature=df1['Result']
        train_output_feature=train_output_feature.replace(-1,0)

        test_input_feature=df2.drop(['Result'],axis=1)
        test_output_feature=df2['Result']
        test_output_feature=test_output_feature.replace(-1,0)

        transformer=self.get_transformer()

        transformed_train_input_feature=transformer.fit_transform(train_input_feature)
        transformed_test_input_feature=transformer.transform(test_input_feature)

        df1=np.c_[transformed_train_input_feature,np.array(train_output_feature)]
        df2=np.c_[transformed_test_input_feature,np.array(test_output_feature)]

        np_array_save(self.dataTransformation.tranformed_train_file_path,df1)
        np_array_save(self.dataTransformation.tranformed_test_file_path,df2)

        save_object(self.dataTransformation.tranformer_file_path,transformer)

        return DataTranformationArtifact(
            self.dataTransformation.tranformed_train_file_path,
            self.dataTransformation.tranformed_test_file_path,
            self.dataTransformation.tranformer_file_path
        )
        return