#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.vpc_stack import VPCStack
from stacks.security_group import SGStack
from stacks.s3_stack import S3Stack


app = cdk.App()
vpc = VPCStack(app, "VPCStack",
)
#sg = SGStack(app, "security", vpc=vpc.vpc)
S3Stack(app, "S3Stack", )

app.synth()
