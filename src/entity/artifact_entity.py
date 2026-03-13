from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    def __init__(self,train_data_path,test_data_path):
        self.train_data_path=train_data_path
        self.test_data_path=test_data_path


class DataValidationArtifact:
    def __init__(self,status,valid_train_data_path,valid_test_data_path,drift_file_path):
        self.status=status
        self.valid_train_data_path=valid_train_data_path
        self.valid_test_data_path=valid_test_data_path
        self.drift_file_path=drift_file_path


@dataclass
class DataTranformationArtifact:
    trans_train_file_path:str
    trans_test_file_path:str
    trand_file_path:str

@dataclass
class ClassficationMetrix:
    f1_score:float
    recall_score:float
    precesion_score:float

@dataclass
class ModelTrainArtifact:
    model_name:str
    model_file_path:str
    train_metrix:ClassficationMetrix
    test_metrix:ClassficationMetrix
