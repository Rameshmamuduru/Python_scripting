import boto3
from botocore import client
from botocore.exceptions import ClientError
import logging
import os


#create a S3 bucket

def create_bucket(bucket_name, region):
    """Create an S3 bucket in a specified region."""
    
    
    s3_client = boto3.client("s3", region_name=region)  
    
    try:
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region}
            )
        return True
    except Exception as e:
        print(f"Error creating bucket: {e}")
        return False

create_bucket("my-bucket", "ap-south-1")


#list a s3 bucket

s3_client = boto3.client ("s3")
list = s3_client.list_buckets ()

print ("existing buckets are: ")

for bucket in list["Buckets"]:
    print (f" {bucket["Name"]}")


# upload a object/file to S3

def upload_file (File_name, Bucket, Object_Name=0):
    
    s3_client = boto3.client ("s3")
    
    if Object_Name is None:
        Object_Name = os.path.basename (File_name)
        
    try:
        Response = s3_client.upload_file(File_name, Bucket, Object_Name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

