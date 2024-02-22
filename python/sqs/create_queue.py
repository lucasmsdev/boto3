import boto3

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName = 'SQS_QUEUE_NAME',
    Attributes={
     'DelaySeconds': '60',
     'MessageRetentionPeriod': '86400'
    }
)

print(response['QueueUrl'])
    