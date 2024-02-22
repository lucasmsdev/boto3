response = client.create_function(
    FunctionName='string',
    Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'nodejs14.x'|'nodejs16.x'|'java8'|'java8.al2'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'python3.9'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'dotnetcore3.1'|'dotnet6'|'dotnet8'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'ruby2.7'|'provided'|'provided.al2'|'nodejs18.x'|'python3.10'|'java17'|'ruby3.2'|'python3.11'|'nodejs20.x'|'provided.al2023'|'python3.12'|'java21',
    Role='string',
    Handler='string',
    Code={
        'ZipFile': b'bytes',
        'S3Bucket': 'string',
        'S3Key': 'string',
        'S3ObjectVersion': 'string',
        'ImageUri': 'string'
    },
    Description='string',
    Timeout=123,
    MemorySize=123,
    Publish=True|False,
    VpcConfig={
        'SubnetIds': [
            'string',
        ],
        'SecurityGroupIds': [
            'string',
        ],
        'Ipv6AllowedForDualStack': True|False
    },
    PackageType='Zip'|'Image',
    DeadLetterConfig={
        'TargetArn': 'string'
    },
    Environment={
        'Variables': {
            'string': 'string'
        }
    },
    KMSKeyArn='string',
    TracingConfig={
        'Mode': 'Active'|'PassThrough'
    },
    Tags={
        'string': 'string'
    },
    Layers=[
        'string',
    ],
    FileSystemConfigs=[
        {
            'Arn': 'string',
            'LocalMountPath': 'string'
        },
    ],
    ImageConfig={
        'EntryPoint': [
            'string',
        ],
        'Command': [
            'string',
        ],
        'WorkingDirectory': 'string'
    },
    CodeSigningConfigArn='string',
    Architectures=[
        'x86_64'|'arm64',
    ],
    EphemeralStorage={
        'Size': 123
    },
    SnapStart={
        'ApplyOn': 'PublishedVersions'|'None'
    },
    LoggingConfig={
        'LogFormat': 'JSON'|'Text',
        'ApplicationLogLevel': 'TRACE'|'DEBUG'|'INFO'|'WARN'|'ERROR'|'FATAL',
        'SystemLogLevel': 'DEBUG'|'INFO'|'WARN',
        'LogGroup': 'string'
    }
)