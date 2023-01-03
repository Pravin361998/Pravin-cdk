from aws_cdk import Stack
import aws_cdk.aws_s3 as s3
from constructs import Construct
class S3Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        aws_s3.Bucket(self,'newbucket',
            bucket_name = 'pravin3443'
        )