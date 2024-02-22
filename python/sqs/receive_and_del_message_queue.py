import boto3

sqs = boto3.client('sqs')

queue_url = 'SQS_QUEUE_URL'


response = sqs.receive_message(
    QueueUrl = queue_url,
    AttributeNames =[
        'SentTimestamp'    
    ],
    MaxNumberOfMessages = 1,
    MessageAttributeNames =[
        'All'
    ],
    VisibilityTimeout = 0,
    WaitTimeSeconds = 0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Deletar a mensagem recebida na fila
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

print('Received and deleted message: %s' % message)