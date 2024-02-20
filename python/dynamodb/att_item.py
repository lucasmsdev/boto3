import boto3

dynamodb = boto3.resource('dynamodb')

my_table = dynamodb.Table('users')

my_table.update_item(
    Key={
        'username': 'lucasmachado',
        'last_name': 'machado'
    },
    UpdateExpression = 'SET age= :val1',
    ExpressionAttributeValues={
        ':val1': 21
    }
)