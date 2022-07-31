# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def delete_security_group(security_group_id):

    try:
        response = vpc_client.delete_security_group(GroupId=security_group_id)

    except ClientError:
        logger.exception('Security group can not be deleted.')
        raise
    else:
        return response


if __name__ == '__main__':
    SECURITY_GROUP_ID = input("Please enter the Security group id")
    security_group = delete_security_group(SECURITY_GROUP_ID)
    logger.info(f'Wow Your security group {SECURITY_GROUP_ID} is deleted successfully.')