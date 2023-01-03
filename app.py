#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.vpc_stack import VPCStack
from stacks.security_group import SGStack
from stacks.s3_stack import S3Stack
from stacks.iam_stack import IAM


app = cdk.App()
vpc = VPCStack(app, "VPCStack",)
#IAM(app, "IAM",)
S3Stack(app, "S3Stack", )

app.synth()
