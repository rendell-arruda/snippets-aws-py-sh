import boto3

regions = ["us-east-1", "sa-east-1"]


tags = {"Produtz": "Issoae", "subProduto": "iagroa"}


def add_tag_log_group(event, context):
    groups_failed_to_tag = []
    # percorre cada região
    for region in regions:
        session = boto3.Session(profile_name="default")
        client_cloudwatch = session.client("logs", region_name=region)

        # lista de log groups da conta
        cloud_watch_list = client_cloudwatch.describe_log_groups()
        # percorre cada log group
        for cloud_watch_log in cloud_watch_list["logGroups"]:
            # pega o namo do logGroup
            logGroupName = cloud_watch_log["logGroupName"]
            try:
                # tenta add tag
                response = client_cloudwatch.tag_log_group(
                    logGroupName=logGroupName, tags=tags
                )
            except Exception as e:
                groups_failed_to_tag.append(logGroupName)
                print(e)
    # print lista de log groups que não foram tagueados
    print("CloudWatch log groups that failed to be tagged:")
    for log_group_name in groups_failed_to_tag:
        print(log_group_name)


if __name__ == "__main__":
    add_tag_log_group({}, {})
