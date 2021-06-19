import os
import boto3
import pytest
from moto import mock_logs

@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    
@pytest.fixture(scope='function')
def cloudwatch_logs(aws_credentials):
    with mock_logs():
        yield boto3.client("logs", region_name='eu-west-1')
        
def test_create_cloudwatch_log_group(cloudwatch_logs):
    """Create Cloudwatch log group"""
    cloudwatch_logs.create_log_group(
        logGroupName='/ecs/mongo/change-stream',
        tags={ 'env': 'test' }
    )

    result = cloudwatch_logs.describe_log_groups()
    assert len(result['logGroups']) == 1
    assert result['logGroups'][0]['logGroupName'] == '/ecs/mongo/change-stream'