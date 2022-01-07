import boto3
import re
import sys

client = boto3.client('wafv2')

ARN = input("Enter Resource ARN --> ")
CHG_NUM = input("Enter Change Request Value --> ")
if not re.match('^[a-zA-Z0-9_]+$', CHG_NUM):
    print("Enter valid change number")
    sys.exit()
while len(CHG_NUM) != 10:
    print("Change number is incorrect length")
    CHG_NUM = input("Enter Change Request Value --> ")

response = client.tag_resource(
    ResourceARN= ARN,
    Tags=[
        {
            'Key': 'LastChangeRequest',
            'Value': CHG_NUM
        },
    ]
)


tag_list = client.list_tags_for_resource(
    ResourceARN=ARN
)

print(tag_list['TagInfoForResource']['TagList'])