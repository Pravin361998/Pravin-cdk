from aws_cdk import  aws_s3, Stack
from constructs import Construct

class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_s3.Bucket(
            self,
            'qwedsazxcde',
            bucket_name = 'qwedsazxcde'
        )