import boto3

sqs = boto3.client('sqs')

queue_url = 'SQS_QUEUE_URL'


response = sqs.send_message(
    QueueUrl = queue_url,
    DelaySeconds = 10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': ' The Whistler'
        },
        'Author':{
            'DataType': 'String',
            'StringValue': 'Lucas Machado'
        },
        'WeeksOn':{
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2006'
    )
)


print(response['MesssageId'])