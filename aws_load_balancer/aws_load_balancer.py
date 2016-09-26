import boto3

# Initialize ec2 resource and elbv2 client
ec2 = boto3.resource('ec2')
elbv2 = boto3.client('elbv2')

# Get all running instances
instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
instance_ids = []
for instance in instances:
    instance_ids.append(instance.id)
    print(instance.id, instance.instance_type)

# Get all AMIs
images = ec2.images.filter(
        Owners=[
            '090475355267',
        ])
image_ids = []
for image in images:
    image_ids.append(image.id)
    print(image.id)
image_id = image_ids[0]

# Create new Server instance
instance = ec2.create_instances(
    ImageId=image_id,
    MinCount=1,
    MaxCount=1,
    KeyName='batman-key-pair-frankfurt',
    SecurityGroups=[
        'default',
    ],
    InstanceType='t2.small',
    Monitoring={
        'Enabled': True
    },
    DisableApiTermination=False,
    InstanceInitiatedShutdownBehavior='stop'
)

# Get new IP Address and add to LoadBalancer's iptables config
a = 0
