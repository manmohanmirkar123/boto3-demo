import boto3

aws_console = boto3.session.Session()

iam_cli = aws_console.client('iam')

for  each in iam_cli.list_users()['Users']:
    print(each['UserName'])