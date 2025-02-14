import boto3

def get_ec2_os(instance_ids, region="us-east-1"):
    ec2 = boto3.client("ec2", region_name=region)
    
    try:
        response = ec2.describe_instances(InstanceIds=instance_ids)
        results = []
        
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                platform_details = instance.get("PlatformDetails", "Linux")
                image_id = instance.get("ImageId", "Desconhecido")
                
                # Buscar detalhes da AMI para obter a versão do sistema operacional
                ami_response = ec2.describe_images(ImageIds=[image_id])
                ami_name = ami_response["Images"][0].get("Name", "Desconhecido")
                
                results.append(f"A instância {instance_id} está rodando: {ami_name} (AMI ID: {image_id}) - {platform_details}")
        
        return "\n".join(results)
    
    except Exception as e:
        return f"Erro ao buscar informações das instâncias: {str(e)}"

# Exemplo de uso
if __name__ == "__main__":
    instance_ids = ["i-00d6ecc704dfe1912", "i-0ead03dea37c61039"]  # Substitua pelos IDs reais
    region = "us-east-1"  # Altere conforme necessário
    print(get_ec2_os(instance_ids, region))