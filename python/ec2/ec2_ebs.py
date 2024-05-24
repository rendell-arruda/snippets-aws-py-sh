import boto3

regions = ["us-east-1"]


def lambda_handler(event, context):

    for region in regions:
        session = boto3.Session(profile_name="default")
        ec2_client = session.client("ec2", region_name=region)

        # describe instance
        instances = ec2_client.describe_instances()
        for reservation in instances["Reservations"]:
            for instance in reservation["Instances"]:
                # listar instanceID
                instanceId = instance["InstanceId"]

                # listar volumes anexados a instancia acima
                volumes = ec2_client.describe_volumes(
                    Filters=[{"Name": "attachment.instance-id", "Values": [instanceId]}]
                )

                for volume in volumes["Volumes"]:
                    volumeId = volume["VolumeId"]
                    print(f" {volumeId} : {instanceId}")


if __name__ == "__main__":
    lambda_handler({}, {})
