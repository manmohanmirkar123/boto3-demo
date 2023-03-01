import boto3

aws_console = boto3.session.Session()
s3_console = aws_console.client('s3')

response = s3_console.create_bucket(Bucket='lr12121212')

print(response)