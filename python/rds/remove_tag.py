import boto3
 
regions = ['us-east-1']
rds_cluster_id = ['db-cartoes1', 'road-map-3']
account_id = '1234567890'


def lambda_handler(event, context):
 
    for region in regions:
        session = boto3.Session(profile_name='default')
        client = session.client('rds',region_name=region)
 
        response = client.list_tags_for_resource(
            ResourceName=f'arn:aws:rds:{region}:{account_id}:db:{rds_cluster_id}'
        )
 
if __name__ == '__main__': lambda_handler({},{})