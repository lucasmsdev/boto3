import boto3


ses = boto3.client('ses')

response = ses.verify_domain_indetity(
    Domain = 'DOMAIN_NAME'
    )
    
print(response)