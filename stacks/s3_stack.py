from aws_cdk import  aws_s3, Stack, Duration
from constructs import Construct

class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_s3.Bucket(
            self,
            'pravin',
            bucket_name = 'pravinnewtest023',
            block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
            versioned=True,
            lifecycle_rules=[
           aws_s3.LifecycleRule(
          enabled=True,
          expiration=Duration.days(365),
          transitions=[
            aws_s3.Transition(
              storage_class=aws_s3.StorageClass.INFREQUENT_ACCESS,
              transition_after=Duration.days(30)
            ),
            aws_s3.Transition(
              storage_class=aws_s3.StorageClass.GLACIER,
              transition_after=Duration.days(90)
            ),
          ]
          
           )
            ]
            

        
        )