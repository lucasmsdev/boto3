import boto3
import logging
from botocore.exceptions import ClientError
import os
import glob

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_files_in_directory(directory, bucket):
    files = glob.glob(os.path.join(directory, '*'))
    for file_name in files:
        success = upload_file(file_name, bucket)
        if success:
            print(f'Sucesso ao carregar {file_name}')
        else:
            print(f'Falha ao carregar {file_name}')

# Exemplo de uso
directory = '/home/ec2-user/environment/s3-bucket-list-jam-logs/'
bucket = 'aws-jam-qualquercoisa'
upload_files_in_directory(directory, bucket)
