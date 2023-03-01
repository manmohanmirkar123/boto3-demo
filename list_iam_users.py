import boto3

aws_console = boto3.session.Session()
iam_console = aws_console.resource('iam')

for users in iam_console.users.all():
    print(users.name)