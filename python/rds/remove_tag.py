import boto3

regions = ['us-east-1']
rds_cluster_id = ['db-cartoes1', 'road-map-3']
account_id = '266549158321'
tag_key = 'environment'

def lambda_handler(event, context):
    for region in regions:
        session = boto3.Session(profile_name='default')
        client = session.client('rds', region_name=region)

        for cluster in rds_cluster_id:
            cluster_arn = f'arn:aws:rds:{region}:{account_id}:db:{cluster}'
            
            response = client.list_tags_for_resource(
                ResourceName=cluster_arn
            )
            
            current_tags = response['TagList']
            # print(f'Tags atuais: {current_tags}\n')
            
            # Encontrar a tag Schedule, se existir
            schedule_tag = next((tag for tag in current_tags if tag["Key"] == tag_key), None)
            
            if schedule_tag:
                client.remove_tags_from_resource(
                    ResourceName=cluster_arn,
                    TagKeys=[tag_key]
                )
                print(f"Tag {tag_key} removida de {cluster}\n")
            else:
                print(f"Tag {tag_key} não encontrada em {cluster}\n")

if __name__ == '__main__':
    lambda_handler({}, {})