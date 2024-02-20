import boto3

# Puxa o serviço
dynamodb = boto3.resource('dynamodb')

# Cria a tabela no DynamoDB
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Verifica se a tabela ja existi
table.wait_until_exists()

# Printa os dados que tem na table( no caso se espera 0 )
print(table.item_count)