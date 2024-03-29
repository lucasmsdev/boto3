import sys 
import boto3
from botocore.exceptions import ClientError

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')

if action == 'ON':
    
    # Primeiro um teste para verificar as permissões
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
        
        
    # Teste feito com sucesso, agora execute as instancias sem teste
    try:
        response = ec2.start_instances(InstaceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

else:
    
    # Teste para verificar as permissões
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if "DryRunOperation" not in str(e):
            raise
        
    
    # Teste feito com sucessp, agore pare as instancias sem teste
    try:
        response = ec2.stop_instances(InstancesIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
    