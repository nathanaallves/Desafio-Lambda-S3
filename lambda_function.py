import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'meu-bucket-exemplo-nathana'
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket_name, Key=key)
    content = response['Body'].read().decode('utf-8')

    # Exemplo de processamento: transformar conteúdo em maiúsculas
    processed_content = content.upper()

    s3.put_object(Bucket=bucket_name, Key=f'processed/{key}', Body=processed_content)
    
    return {
        'statusCode': 200,
        'body': f'Arquivo {key} processado com sucesso!'
    }
