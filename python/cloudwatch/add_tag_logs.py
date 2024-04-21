import boto3

regions = ["us-east-1", "sa-east-1"]


tags = {"Produtz": "Issoae", "subProduto": "iagroa"}


def lambda_handler(event, context):

    for region in regions:
        session = boto3.Session(profile_name="default")
        client_cloudwatch = session.client("logs", region_name=region)

        cloud_watch_list = client_cloudwatch.describe_log_groups()
        for cloud_watch_log in cloud_watch_list["logGroups"]:
            logGroupName = cloud_watch_log["logGroupName"]

            # add tag
            response = client_cloudwatch.tag_log_group(
                logGroupName=logGroupName, tags=tags
            )


if __name__ == "__main__":
    lambda_handler({}, {})
