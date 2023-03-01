import boto3

aws_console = boto3.session.Session()
s3_console = aws_console.resource('s3')

for i in s3_console.buckets.all():
    print(i.name)