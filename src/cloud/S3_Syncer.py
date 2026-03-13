import os
from src.exception import NetworkSecurityException
import sys
import subprocess

class S3_Sync:
    def __init__(self):
        pass
    def sync_to_s3(self,folder,s3_url):
        try:
           os.system(f'aws s3 sync {folder} {s3_url}')
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def sync_from_s3(self,folder,s3_url):
        try:
            os.system(f"aws s3 sync {s3_url} {folder}")
        except Exception as e:
            raise NetworkSecurityException(e,sys)