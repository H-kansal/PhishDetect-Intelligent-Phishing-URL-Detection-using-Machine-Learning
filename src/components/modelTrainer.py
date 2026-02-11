import os
import numpy as np
import pandas as pd
from src.exception import NetworkSecurityException
from src.logger import logging
from src.entity.config_entity import ModelTrainingConfig
from src.utils.file_utils_functions import np_array_load,Evaluate_models,Evaluation_matrix,save_object
from  src.entity.artifact_entity import ModelTrainArtifact
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from src.entity.artifact_entity import ModelTrainArtifact
import dagshub
import mlflow
from urllib.parse import urlparse


dagshub.init(repo_owner='H-kansal', repo_name='my-first-repo', mlflow=True)


class ModelTraining:
    def __init__(self,tranformationArtifact):
        self.tranformationArtifact=tranformationArtifact
        self.modelTrainingConfig=ModelTrainingConfig()
    

    def track_mlflow(self, best_model, classificationmetric):

        # Set DagsHub tracking URI
        mlflow.set_tracking_uri("https://dagshub.com/<username>/<repo_name>.mlflow")

        with mlflow.start_run():

            mlflow.log_metric("f1_score", classificationmetric.f1_score)
            mlflow.log_metric("precision", classificationmetric.precision_score)
            mlflow.log_metric("recall_score", classificationmetric.recall_score)

            mlflow.sklearn.log_model(
                sk_model=best_model,
                name="model",
                serialization_format="cloudpickle"
            )




    def train_models(self,X_train,y_train,X_test,y_test):

        models={
            "LogisticRegression":LogisticRegression(),
            "KNeighborsClassifier":KNeighborsClassifier(),
            "DecisionTreeClassifier":DecisionTreeClassifier(),
            "RandomForestClassifier":RandomForestClassifier(),
            "AdaBoostClassifier":AdaBoostClassifier(),
            "GradientBoostingClassifier":GradientBoostingClassifier()
        }

        best_model,report,model_name=Evaluate_models(models,X_train,y_train,X_test,y_test)

        print(f"Model Report:{report}")

        y_train_pred=best_model.predict(X_train)
        y_test_pred=best_model.predict(X_test)

        test_evaluation_metrix=Evaluation_matrix(y_train_pred,y_train)
        self.track_mlflow(model_name,test_evaluation_metrix)


        train_evaluation_metrix=Evaluation_matrix(y_test_pred,y_test)
        self.track_mlflow(model_name,train_evaluation_metrix)

        save_object(self.modelTrainingConfig.model_file_path,best_model)

        return ModelTrainArtifact(model_name=model_name,model_file_path=self.modelTrainingConfig.model_file_path,     train_metrix=train_evaluation_metrix,test_metrix=test_evaluation_metrix)


    def intialize_model_training(self):
        train_file_path=self.tranformationArtifact.trans_train_file_path
        test_file_path=self.tranformationArtifact.trans_test_file_path

        train=np_array_load(train_file_path)
        test=np_array_load(test_file_path)
        
        X_train,y_train,X_test,y_test=(
            train[:,:-1],
            train[:,-1],
            test[:,:-1],
            test[:,-1]
        )
        
        modelArtifact=self.train_models(X_train,y_train,X_test,y_test)
        print(modelArtifact)
        return modelArtifact