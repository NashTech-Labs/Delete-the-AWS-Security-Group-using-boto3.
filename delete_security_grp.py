# by MuZakkir Saifi

# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError

REGION = input("Please enter the AWS REGION")

# this is the configration for the logger

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

subnet_client = boto3.client("ec2", region_name=REGION)


def delete_group(group_id):

    try:
        res = subnet_client.delete_security_group(GroupId=group_id)

    except ClientError:
        logger_for.exception('Security group can not be deleted.')
        raise
    else:
        return res


if __name__ == '__main__':
    GRP_ID = input("Please enter the Security group id")   
    security_group = delete_group(GRP_ID)
    logger_for.info(f'Wow Your security group {GRP_ID} is deleted successfully.')