import boto3

ecs = boto3.client('ecs')

response = ecs.update_cluster(
    cluster = '<string>',
    settings = [
        {
            'name': 'containerInsights',
            'value': '<string>'
        }
    ]
    configuration = {
        'executeCommandConfiguration': {
            'kmsKeyId': '<string>',
            'logging': 'NONE'| 'DEFAULT' | 'OVERRIDE',
            'logConfiguration': {
                'cloudWatchLogGroupName': '<string>',
                'cloudWatchEncryptionEnabled': True|False,
                's3BucketName': '<string>',
                's3EncryptionEnabled': True|False,
                's3KeyPrefix': '<string>'
            }
        }
    },
    serviceConnectDefaults={
        'namespace':'<string>'
    }
)