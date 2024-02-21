import boto3


ses = boto3.client('ses')

response = ses.list_templates(
  MaxItems=10
)

print(response)