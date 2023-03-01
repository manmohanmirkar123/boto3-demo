import boto3

aws_console = boto3.session.Session()
ec2_mgmt_cli = aws_console.client(service_name='ec2')

res = ec2_mgmt_cli.run_instances(ImageId='ami-0dfcb1ef8550277af',InstanceType='t2.micro',MaxCount=2,MinCount=1)
print(res)
