from aws_cdk import Stack
import aws_cdk.aws_ec2 as ec2
from constructs import Construct
class VPCStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(self, "Vpc",
    cidr="10.0.0.0/24"
)
