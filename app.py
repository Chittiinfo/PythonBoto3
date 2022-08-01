import boto3
import re
from pprint import pprint
regions=[]
client = boto3.client('ec2',region_name='us-east-1')
VPCs=client.describe_vpcs()
regions=client.describe_regions()
iam= boto3.client('iam')
roles=iam.list_roles().get('roles',[])
for role in roles:
    print(role['RoleName'])
    print(100*'-')
#print(VPCs)
#print(regions)

  