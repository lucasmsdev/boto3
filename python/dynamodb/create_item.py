import boto3


dynamodb = boto3.resource('dynamodb')

my_table = dynamodb.Table('users')

my_table.put_item(
    Item={
        'username': 'lucasmachado',
        'first_name': 'lucas',
        'last_name': 'machado',
        'age': 19,
        'account-type': 'standart-user'
    }
)


 