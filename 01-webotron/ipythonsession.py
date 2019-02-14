# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)

new_bucket = s3.create_bucket(Bucket='yingying5-ipython', CreateBucketConfiguration = {'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='yingying5-ipython', CreateBucketConfiguration = {'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='yingying5-ipython', CreateBucketConfiguration = {'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='yingying5-ipython')
for bucket in s3.buckets.all():
    print(bucket)


import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
for i in ec2.instances.all():
    print(i)
$history
