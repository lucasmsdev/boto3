import boto3

ecs = boto3.client('ecs')

response = ecs.create_cluster(
    clusterName='string',
    tags=[
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    settings=[
        {
            'name': 'containerInsights',
            'value': 'string'
        },
    ],
    configuration={
        'executeCommandConfiguration': {
            'kmsKeyId': 'string',
            'logging': 'NONE'|'DEFAULT'|'OVERRIDE',
            'logConfiguration': {
                'cloudWatchLogGroupName': 'string',
                'cloudWatchEncryptionEnabled': True|False,
                's3BucketName': 'string',
                's3EncryptionEnabled': True|False,
                's3KeyPrefix': 'string'
            }
        }
    },
    capacityProviders=[
        'string',
    ],
    defaultCapacityProviderStrategy=[
        {
            'capacityProvider': 'string',
            'weight': 123,
            'base': 123
        },
    ],
    serviceConnectDefaults={
        'namespace': 'string'
    }
)