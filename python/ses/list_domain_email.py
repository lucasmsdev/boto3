import boto3

ses = boto3.client('ses')

response = ses.list_identities(
    IdentityType = 'Domain',
    MaxItems = 10
)

print(response)