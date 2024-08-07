import boto3
import logging
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    
    # Se o object_name não for especificado, use o file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
        
    # Upload do arquivo    
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True