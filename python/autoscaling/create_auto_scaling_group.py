import boto3 

auto_scaling = boto3.client('autoscaling')

response = auto_scaling.create_auto_scaling_group(
    AutoScalingGroupName='string',
    LaunchConfigurationName='string',
    LaunchTemplate={
        'LaunchTemplateId': 'string',
        'LaunchTemplateName': 'string',
        'Version': 'string'
    },
    MixedInstancesPolicy={
        'LaunchTemplate': {
            'LaunchTemplateSpecification': {
                'LaunchTemplateId': 'string',
                'LaunchTemplateName': 'string',
                'Version': 'string'
            },
            'Overrides': [
                {
                    'InstanceType': 'string',
                    'WeightedCapacity': 'string',
                    'LaunchTemplateSpecification': {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'Version': 'string'
                    },
                    'InstanceRequirements': {
                        'VCpuCount': {
                            'Min': 123,
                            'Max': 123
                        },
                        'MemoryMiB': {
                            'Min': 123,
                            'Max': 123
                        },
                        'CpuManufacturers': [
                            'intel'|'amd'|'amazon-web-services',
                        ],
                        'MemoryGiBPerVCpu': {
                            'Min': 123.0,
                            'Max': 123.0
                        },
                        'ExcludedInstanceTypes': [
                            'string',
                        ],
                        'InstanceGenerations': [
                            'current'|'previous',
                        ],
                        'SpotMaxPricePercentageOverLowestPrice': 123,
                        'MaxSpotPriceAsPercentageOfOptimalOnDemandPrice': 123,
                        'OnDemandMaxPricePercentageOverLowestPrice': 123,
                        'BareMetal': 'included'|'excluded'|'required',
                        'BurstablePerformance': 'included'|'excluded'|'required',
                        'RequireHibernateSupport': True|False,
                        'NetworkInterfaceCount': {
                            'Min': 123,
                            'Max': 123
                        },
                        'LocalStorage': 'included'|'excluded'|'required',
                        'LocalStorageTypes': [
                            'hdd'|'ssd',
                        ],
                        'TotalLocalStorageGB': {
                            'Min': 123.0,
                            'Max': 123.0
                        },
                        'BaselineEbsBandwidthMbps': {
                            'Min': 123,
                            'Max': 123
                        },
                        'AcceleratorTypes': [
                            'gpu'|'fpga'|'inference',
                        ],
                        'AcceleratorCount': {
                            'Min': 123,
                            'Max': 123
                        },
                        'AcceleratorManufacturers': [
                            'nvidia'|'amd'|'amazon-web-services'|'xilinx',
                        ],
                        'AcceleratorNames': [
                            'a100'|'v100'|'k80'|'t4'|'m60'|'radeon-pro-v520'|'vu9p',
                        ],
                        'AcceleratorTotalMemoryMiB': {
                            'Min': 123,
                            'Max': 123
                        },
                        'NetworkBandwidthGbps': {
                            'Min': 123.0,
                            'Max': 123.0
                        },
                        'AllowedInstanceTypes': [
                            'string',
                        ]
                    }
                },
            ]
        },
        'InstancesDistribution': {
            'OnDemandAllocationStrategy': 'string',
            'OnDemandBaseCapacity': 123,
            'OnDemandPercentageAboveBaseCapacity': 123,
            'SpotAllocationStrategy': 'string',
            'SpotInstancePools': 123,
            'SpotMaxPrice': 'string'
        }
    },
    InstanceId='string',
    MinSize=123,
    MaxSize=123,
    DesiredCapacity=123,
    DefaultCooldown=123,
    AvailabilityZones=[
        'string',
    ],
    LoadBalancerNames=[
        'string',
    ],
    TargetGroupARNs=[
        'string',
    ],
    HealthCheckType='string',
    HealthCheckGracePeriod=123,
    PlacementGroup='string',
    VPCZoneIdentifier='string',
    TerminationPolicies=[
        'string',
    ],
    NewInstancesProtectedFromScaleIn=True|False,
    CapacityRebalance=True|False,
    LifecycleHookSpecificationList=[
        {
            'LifecycleHookName': 'string',
            'LifecycleTransition': 'string',
            'NotificationMetadata': 'string',
            'HeartbeatTimeout': 123,
            'DefaultResult': 'string',
            'NotificationTargetARN': 'string',
            'RoleARN': 'string'
        },
    ],
    Tags=[
        {
            'ResourceId': 'string',
            'ResourceType': 'string',
            'Key': 'string',
            'Value': 'string',
            'PropagateAtLaunch': True|False
        },
    ],
    ServiceLinkedRoleARN='string',
    MaxInstanceLifetime=123,
    Context='string',
    DesiredCapacityType='string',
    DefaultInstanceWarmup=123,
    TrafficSources=[
        {
            'Identifier': 'string',
            'Type': 'string'
        },
    ],
    InstanceMaintenancePolicy={
        'MinHealthyPercentage': 123,
        'MaxHealthyPercentage': 123
    }
)