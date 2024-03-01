import boto3

auto_scaling = boto3.client('autoscaling')

response = auto_scaling.delete_auto_scaling_group(
    AutoScalingGroupName = '<string>',
    ForceDelete = True|False
)