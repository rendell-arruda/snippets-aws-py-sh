import boto3
 
regions = ['us-east-1']
rds_cluster_id = ['db-cartoes1', 'road-map-3']
account_id = '266549158321'


def lambda_handler(event, context):
 
    for region in regions:
        session = boto3.Session(profile_name='default')
        client = session.client('rds',region_name=region)

        for cluster in rds_cluster_id:
            response = client.list_tags_for_resource(
                ResourceName=f'arn:aws:rds:{region}:{account_id}:db:{cluster}'
            )
            current_tags = response['TagList']
            print(f'{current_tags}\n')
            
            schedule_tag= next((tag for tag in current_tags if tag["Key"] == 'Schedule'), 'Tag schedule not found')
            
            print(f'{schedule_tag}\n')
            
 
if __name__ == '__main__': lambda_handler({},{})