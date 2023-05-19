import os
import boto3


def upload_folder_to_s3(bucket_name, folder_path):
    s3 = boto3.client("s3")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            s3.upload_file(file_path, bucket_name, file_path)
