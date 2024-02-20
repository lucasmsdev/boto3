import boto3

dynamodb = boto3.resource('dynamodb')

my_table = dynamodb.Table('users')

response = my_table.get_item(
    Key={
        'username': 'lucasmachado',
        'last_name': 'machado'
    }
)

if 'Item' in response:
    item = response['Item']
    print(item)
else:
    print('Não há nenhum item nesta tabela com essas chaves')

