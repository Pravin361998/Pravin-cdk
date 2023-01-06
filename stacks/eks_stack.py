from aws_cdk import  Stack
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_eks as eks
import aws_cdk.aws_iam as iam

from constructs import Construct
class EKSStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

##Vpc creation

        vpc = ec2.Vpc(self, "VPC",
                           max_azs=2,
                           ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
                           # configuration will create 3 groups in 2 AZs = 6 subnets.
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public",
                               cidr_mask=24
                           ),
                           ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                               name="Private",
                               cidr_mask=24
                           )
                           ]
        )

#IAM role creation for node group
        eksNG_role = iam.Role(self, "nodegrouprole", 
                               assumed_by=iam.ServicePrincipal(service='ec2.amazonaws.com'),
                               role_name='eks-cluster-role',
                               managed_policies=[
                               iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKSWorkerNodePolicy"),
                               iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKSClusterPolicy"),
                               iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2ContainerRegistryReadOnly"),
                               iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEKS_CNI_Policy"),
            ]
            )
      

#Cluster Creation
        cluster = eks.Cluster(self, 'Cluster',
                              cluster_name = "Pravincluster",
                              vpc=vpc,
                              version=eks.KubernetesVersion.V1_24,
                              endpoint_access=eks.EndpointAccess.PUBLIC_AND_PRIVATE,
                              default_capacity=0
                              )
#Nodegroup Creation      
        nodegroup = eks.Nodegroup(self, "Nodegroup",
                                 cluster=cluster,
                                 ami_type=eks.NodegroupAmiType.AL2_X86_64,
                                 capacity_type=eks.CapacityType.ON_DEMAND,
                                 instance_types=[ec2.InstanceType('t3a.medium')],
                                 disk_size=20,
                                 desired_size=2,
                                 max_size=2,
                                 min_size=2,
                                 node_role=eksNG_role,
                                
        )


