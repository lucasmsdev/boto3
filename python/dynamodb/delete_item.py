import boto3

dynamodb = boto3.resource('dynamodb')

my_table = dynamodb.Table('users')

my_table.delete_item(
    Key={
        'username': 'lucasmachado',
        'last_name': 'machado'
    }    
)