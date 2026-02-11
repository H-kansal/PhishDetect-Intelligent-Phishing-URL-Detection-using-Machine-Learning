import numpy as np


DB_NAME="NetworkData"
DB_COLLECTION="network_data"
FEATURE_COLLECTION_NAME="featured_data.csv"
TRAIN_COLLECTION_NAME="train_data.csv"
TEST_COLLECTION_NAME="test_data.csv"
DATA_DIR="artifact"
INGESTION_DATA_DIR="ingestionData"
VALID_DATA_DIR="validData"
VALID_TEST_COLLECTION_NAME='valid_test_data.csv'
VALID_TRAIN_COLLECTION_NAME='valid_train_data.csv'
DRIFT_FILE_PATH='drift_file_path.yaml'
TRANSFORMATION_DIR='tranformationData'
TRANSFORM_TRAIN_COLLECTION_NAME='tranformed_train_data.csv'
TRANSFORM_TEST_COLLECTION_NAME='tranformed_test_data.csv'
TRANSFORMER_FILE='transformer_file.pkl'
TARGET_FEATURE='Result'
IMPUTER_PARAMS={
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
TRAINING_DIR='model_training'
MODEL_FILE_PATH='model.pkl'