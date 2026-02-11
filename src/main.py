from src.exception import NetworkSecurityException
from src.logger import logging
from src.components.dataIngestion import DataIngestion
from src.components.datavalidation import DataValidation
from src.components.dataTransformation import DataTransformation
from src.components.modelTrainer import ModelTraining
import sys




if __name__ == '__main__':
    try:
        # Data Ingestion
        data_ingestion = DataIngestion()
        ingestion_artifact = data_ingestion.intialize_data_ingestion()

        logging.info(
            f"Train path: {ingestion_artifact.train_data_path}, "
            f"Test path: {ingestion_artifact.test_data_path}"
        )

        # Data Validation
        data_validation = DataValidation(ingestion_artifact)
        validation_artifact = data_validation.intialize_validation_data()

        logging.info(f"Data validation artifact: {validation_artifact}")
        
        #Data Tranformation
        data_transformation=DataTransformation(validation_artifact)
        transformation_artifact=data_transformation.intialize_tranformation()

        print(transformation_artifact)

        #Model Training
        model_training=ModelTraining(transformation_artifact)
        model_artifact=model_training.intialize_model_training()
    except Exception as e:
        raise NetworkSecurityException(e, sys)