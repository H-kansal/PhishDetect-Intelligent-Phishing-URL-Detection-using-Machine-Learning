from src.components.dataIngestion import DataIngestion
from src.components.datavalidation import DataValidation
from src.components.dataTransformation  import DataTransformation
from src.components.modelTrainer import ModelTraining
from src.exception import NetworkSecurityException
from src.cloud.S3_Syncer import S3_Sync
from src.constants import training
import sys
import os


class Training:
    def __init__(self):
        self.s3_sync=S3_Sync()

    def start_data_ingestion(self):
        try:
            data_ingestion=DataIngestion()
            ingestion_artifact=data_ingestion.intialize_data_ingestion()
            return ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_data_validation(self,ingestion_artifact):
        try:
            data_validation=DataValidation(ingestion_artifact)
            validation_artifact=data_validation.intialize_validation_data()
            return validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_data_transformation(self,validation_artifact):
        try:
            data_transfomation=DataTransformation(validation_artifact)
            return data_transfomation.intialize_tranformation()
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_model_trainer(self,tranformation_artifact):
        try:
            model_trainer=ModelTraining(tranformation_artifact)
            return model_trainer.intialize_model_training()
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def sync_artifact_to_s3(self):
        try:
            s3_url=f"s3://{training.S3_BUCKET_NAME}/artifact"
            self.s3_sync.sync_to_s3("artifact",s3_url)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def start_training_pipeline(self):
        try:
            ingestion_artifact=self.start_data_ingestion()
            validation_artifact=self.start_data_validation(ingestion_artifact)
            tranformation_artifact=self.start_data_transformation(validation_artifact)
            modelTraining_artifact=self.start_model_trainer(tranformation_artifact)
            self.sync_artifact_to_s3()
            return modelTraining_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)