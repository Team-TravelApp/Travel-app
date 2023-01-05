import boto3
import boto.s3.connection
access_key = 'AKIA3UU7OFV6HPTF3645'
secret_key = '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'

# creates a connection with the s3 server
conn = boto.connect_s3(
        aws_access_key_id='AKIA3UU7OFV6HPTF3645',
        aws_secret_access_key='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',
        host='objects.dreamhost.com',
        is_secure=False,
        calling_format=boto.s3.connection.OrdinaryCallingFormat(),
        )

s3 = boto3.resource
