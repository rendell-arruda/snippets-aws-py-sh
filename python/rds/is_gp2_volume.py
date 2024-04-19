import boto3

session = boto3.Session(profile_name="default")


def is_gp2_volume(volume_type):
    return volume_type == "gp2"


def describe_rds_volumes(region):
    print(f"Entrando na região {region}\n")
    rds_client = session.client("rds", region_name=region)

    paginator = rds_client.get_paginator("describe_db_instances")
    page_iterator = paginator.paginate()

    for page in page_iterator:
        for db_instance in page["DBInstances"]:
            instance_id = db_instance["DBInstanceIdentifier"]
            storage_type = db_instance["StorageType"]

            if is_gp2_volume(storage_type):
                print(
                    f"A instância RDS {instance_id} está utilizando um volume EBS do tipo gp2."
                )
            else:
                print(
                    f"A instância RDS {instance_id} não está utilizando um volume EBS do tipo gp2."
                )


regions = ["us-east-1", "sa-east-1"]

for region in regions:
    describe_rds_volumes(region)
