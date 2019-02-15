import boto3,os
os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
s3 = boto3.client('s3', 'us-west-2')
s3.create_bucket(Bucket='my-bucket-rupin',
                 CreateBucketConfiguration={'LocationConstraint': "us-west-2"}
                 )
