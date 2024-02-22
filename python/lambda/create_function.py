 import boto3
 
 client_lambda = boto3.client('lambda')
 
 response = client.create_function(
    FunctionName = '<string>',
    Runtime = 'nodejs'|'nodejs14.x',
    Role = '<string>',
    Handler = '<string>'
    Code={
        'ZipFile' : b'bytes',
        'S3Bucket': '<string>',
        'S3Key': '<string>',
        'S3ObjectVersion': '<string>',
        'ImageUri': '<string>'
    },
    Description='<string>',
    Timeout = 120,
    MemorySize = 123,
    Publish = True|False,
    VpcConfig = {
        'SubnetoIds': [
            '<string>',
        ],
        'SecurityGroup': [
            '<string>'
        ]
        'Ipv6AllowedForDualStack': True|False
    },
    PackageType = 'Zip'|'Image',
    DeadLetterConfig = {
        'TargetArn': '<string>'
    },
    Environment={
        'Variables': {
            '<string>': '<string>'
        }
    },
    KMSKeyArn='<string>',
    TracingConfig={
        'Mode': 'Active'|'PassThrough'    
    },
    Tags={
        '<string>': '<string>'
    },
    Layers =[
        '<string>'
    ],
    FileSystemConfigs=[
        {
            'Arn':'<string>',
            'LocalMounthPath':'<string>'
        },
    ],
    ImageConfig={
        'EntryPoint':[
            '<string>'    
        ],
        'Command': [
            '<string>'
        ],
        'WorkingDirectory' : '<string>'
    },
    CodeSigninConfigArn='<string>',
    Architectures=[
        'x86_64' | 'arm64'
    ],
    EphemeralStorage={
        'Size': 123
    },
    SnapStart={
        'ApplyOn': 'PublishedVersions' | 'None'
    }
)