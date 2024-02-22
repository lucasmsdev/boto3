import boto3

sqs = boto3.client('sqs')

sqs.delete_queue(QueueUrl='SQS_QUEUE_URL')