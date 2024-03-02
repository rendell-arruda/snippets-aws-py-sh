import boto3

snapshot_ids = ["snap-07342d2790f28cf8a", "snap-0e7324777f6789ee0"]
ec2_client = boto3.client("ec2")

response = ec2_client.describe_snapshots(SnapshotIds=snapshot_ids)
snapshots_info = response["Snapshots"]

for snapshot_info in snapshots_info:
    print(f"Snapshot ID: {snapshot_info['SnapshotId']} ")
    print(f"Description: {snapshot_info.get('Description', 'N/A')}")
    print("----")
