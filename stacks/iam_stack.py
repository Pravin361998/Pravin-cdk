from aws_cdk import  aws_iam, Stack
from constructs import Construct

class IAM(Stack):
      def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        user = IAM.User(self, "MyUser",
             user_name="Pravin")