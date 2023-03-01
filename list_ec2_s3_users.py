import boto3

aws_console = boto3.session.Session()
user_session_cli = aws_console.client(service_name= 'iam')

response = user_session_cli.list_users()

for each in response['Users']:
    print(each['UserName'])
    
    
ec2_session_cli = aws_console.client(service_name= 'ec2')

response = ec2_session_cli.describe_instances()

for each in response['Reservations']:
    for instance in each['Instances']:
        print(instance['InstanceId'])
        
    
s3_session_cli = aws_console.client(service_name= 's3')

response = s3_session_cli.list_buckets()
for each in response['Buckets']:
    print(each['Name'])
    


        