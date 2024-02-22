import boto3

sqs = boto3.client('sqs')

response = sqs.get_queue_url(QueueName='SQS_QUEUE_NAME')

print(response['QueueUrl'])