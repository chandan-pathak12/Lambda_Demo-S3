import json
import boto3

def lambda_handler(event, context):
    source_bucket = 'jaipurlambda'
    destination_bucket = 'destinationresult'

    s3 = boto3.client('s3')

    # List objects in the source bucket
    objects = s3.list_objects(Bucket=source_bucket)['Contents']

    # Copy each object from the source to the destination bucket
    for obj in objects:
        copy_source = {'Bucket': source_bucket, 'Key': obj['Key']}
        destination_key = obj['Key']
        s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=destination_key)

    return {
        'statusCode': 200,
        'body': 'S3 copy operation complete'
    }