import boto3 

lambda_client = boto3.client('lambda')

response = lambda_client(
    FunctionName = '<string>',
    Qualifier = '<string>'
)