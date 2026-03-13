import os
from src.exception import NetworkSecurityException
import sys
import yaml
import numpy as np
import pickle
from sklearn.metrics import r2_score,precision_score,f1_score,recall_score
from src.entity.artifact_entity import ClassficationMetrix




def read_yaml_file(path:str):
    try:
        print("file Path",path)
        with open(path,'rb') as read_yaml:
            return yaml.safe_load(read_yaml)
    except Exception as e:
        raise NetworkSecurityException(e,sys)


def write_yaml_file(path:str,content):
    file_dir=os.path.dirname(path)
    os.makedirs(file_dir,exist_ok=True)
    with open(path,'w') as write_yaml:
        yaml.dump(content,write_yaml)
    return

def np_array_save(path:str,df):
    try:
        dir_name=os.path.dirname(path)
        os.makedirs(dir_name,exist_ok=True)
        with open(path,'wb') as file:
            np.save(file,df)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def np_array_load(path:str):
    try:
        dir_name=os.path.dirname(path)
        os.makedirs(dir_name,exist_ok=True)
        with open(path,'rb') as file:
            return np.load(file)
    except Exception as e:
        NetworkSecurityException(e,sys)


def save_object(path:str,obj):
    try:
        dir_name=os.path.dirname(path)
        os.makedirs(dir_name,exist_ok=True)
        with open(path,'wb') as file:
            pickle.dump(obj,file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)

def load_object(path:str):
    try:
        with open(path,'rb') as file:
            return pickle.load(file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)


def Evaluate_models(models,X_train,y_train,X_test,y_test):
    try:
        report={}
        best_score=-np.inf
        best_model=None
        best_model_name=None
        for i in range(len(list(models))):
            curr_model=list(models.values())[i]
            curr_model.fit(X_train,y_train)

            y_train_pred=curr_model.predict(X_train)
            y_test_pred=curr_model.predict(X_test)

            train_r2_score=r2_score(y_train,y_train_pred)
            test_r2_score=r2_score(y_test,y_test_pred)

            if test_r2_score>best_score:
                best_score=test_r2_score
                best_model=curr_model
                best_model_name=list(models.keys())[i]

            report[list(models.keys())[i]]=test_r2_score
        return best_model,report,best_model_name
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def Evaluation_matrix(y_pred,y_actual):
    try:
        model_precision_score=precision_score(y_actual,y_pred)
        model_recall_score=recall_score(y_actual,y_pred)
        model_f1_score=f1_score(y_actual,y_pred)
        return ClassficationMetrix(recall_score=model_recall_score,precesion_score=model_precision_score,f1_score=model_f1_score)
    except Exception as e:
        raise NetworkSecurityException(e,sys)

