#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.vpc_stack import VPCStack
from stacks.s3_stack import S3Stack
from stacks.vpc_ec2_stack import EC2VpcStack
from stacks.eks_stack import EKSStack

app = cdk.App()
vpc = VPCStack(app, "VPCStack",)
ec2 = EC2VpcStack(app, "EC2VpcStack", )
s3 = S3Stack(app, "S3Stack")
eks = EKSStack(app, "EKSStack")


app.synth()
