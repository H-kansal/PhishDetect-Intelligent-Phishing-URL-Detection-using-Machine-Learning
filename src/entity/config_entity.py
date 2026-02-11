from src.constants import training
import os


class DataIngestionConfig:
    def __init__(self):
        self.database=training.DB_NAME
        self.collection=training.DB_COLLECTION
        self.data_dir=training.DATA_DIR
        self.ingestion_data_dir=os.path.join(self.data_dir,training.INGESTION_DATA_DIR)
        self.featured_file_path=os.path.join(self.ingestion_data_dir,training.FEATURE_COLLECTION_NAME)
        self.train_file_path=os.path.join(self.ingestion_data_dir,training.TRAIN_COLLECTION_NAME)
        self.test_file_path=os.path.join(self.ingestion_data_dir,training.TEST_COLLECTION_NAME)
        self.train_test_ratio=0.8


class DataValidationConfig:
    def __init__(self):
        self.validation_status=True
        self.data_dir=training.DATA_DIR
        self.invalid_dir=os.path.join(self.data_dir,training.INGESTION_DATA_DIR)
        self.valid_dir=os.path.join(self.data_dir,training.VALID_DATA_DIR)
        self.invalid_train_file_path=os.path.join(self.invalid_dir,training.TRAIN_COLLECTION_NAME)
        self.invalid_test_file_path=os.path.join(self.invalid_dir,training.TEST_COLLECTION_NAME)
        self.valid_train_file_path=os.path.join(self.valid_dir,training.VALID_TRAIN_COLLECTION_NAME)
        self.valid_test_file_path=os.path.join(self.valid_dir,training.VALID_TEST_COLLECTION_NAME)
        self.drift_file_path=os.path.join(self.data_dir,'drift',training.DRIFT_FILE_PATH)

class DataTransformationConfig:
    def __init__(self):
        self.data_dir=training.DATA_DIR
        self.tranformation_dir=os.path.join(self.data_dir,training.TRANSFORMATION_DIR)
        self.tranformed_train_file_path=os.path.join(self.tranformation_dir,training.TRANSFORM_TRAIN_COLLECTION_NAME)
        self.tranformed_test_file_path=os.path.join(self.tranformation_dir,training.TRANSFORM_TEST_COLLECTION_NAME)
        self.tranformer_file_path=os.path.join(self.tranformation_dir,training.TRANSFORMER_FILE)

class ModelTrainingConfig:
    def __init__(self):
        self.data_dir=training.DATA_DIR
        self.training_dir=os.path.join(self.data_dir,training.TRAINING_DIR)
        self.model_file_path=os.path.join(self.training_dir,training.MODEL_FILE_PATH)