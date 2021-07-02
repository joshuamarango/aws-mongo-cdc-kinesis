import os
import boto3
import pytest
import moto


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture(scope='function')
def dynamodb(aws_credentials):
    with moto.mock_dynamodb2():
        yield boto3.client("dynamodb", region_name='eu-west-1')


def test_create_dynamodb_table(dynamodb):
    """Create Cloudwatch log group"""
    pass
