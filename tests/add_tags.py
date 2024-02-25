import boto3

session = boto3.Session(profile_name='default')

client = session.client('resourcegroupstaggingapi')
# arn fora do padrao nao funciona
arn_teste = 'arn:aws:payments::22222222222:payment-instrument:6ce13232-aaaaa-4c45-94ab-xxxxxxxxxxxx'

response = client.tag_resources(
    ResourceARNList=[
        arn_teste,
    ],
    Tags={
        'map': 'migrated'
    }
)
