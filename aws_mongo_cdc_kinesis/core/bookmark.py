import boto3
from botocore.client import BaseClient


class StreamBookmark:
    def __init__(self):
        self.dynamo: BaseClient = boto3.client("dynamo")

    def save(self, resume_token: str) -> None:
        """Save resume_token to DynamoDB"""
        try:
            self.dynamo.insert_item(data=resume_token)
        except:
            print("error saving bookmark")
