# Lambda-DynamoDB
Criar uma função Lambda que:  Incrementa um contador sempre que for chamada  Armazena e lê o valor atual de um item no DynamoDB
# 📍 Etapas do Lab
1. Criar a tabela no DynamoDB
Vá ao console da AWS > procure por DynamoDB

Clique em "Create table"

Table name: ContadorAcessos

Partition key: id (tipo: String)

Mantenha o resto como padrão (modo On-demand)

📌 Importante: A tabela será criada com acesso automático Free Tier

# 2. Criar a função Lambda
Vá para Lambda > Create function

Name: contadorLambda

Runtime: Python 3.12

Role: Crie nova com permissões básicas

Substitua o código da função por este:

python

import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContadorAcessos')

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'acessos'},
        UpdateExpression='ADD #contador :incremento',
        ExpressionAttributeNames={'#contador': 'contador'},
        ExpressionAttributeValues={':incremento': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    novo_valor = response['Attributes']['contador']
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'acessos': int(novo_valor)})
    }
Clique em Deploy

# 3. Dar permissão para acessar o DynamoDB
Vá em "Configuration" > "Permissions" > clique no Role

Em "Permissions policies", clique em "Add permissions" > "Attach policies"

Busque por AmazonDynamoDBFullAccess e anexe a política (para lab, é suficiente)

# 4. Criar a API Gateway
Volte na função Lambda > clique em "Adicionar gatilho"

Selecione API Gateway

Tipo: HTTP API

Segurança: Open

Clique em "Add"

5. Testar no navegador
Acesse a URL pública gerada pelo API Gateway.
A cada chamada, o contador será incrementado e retornará algo como:

json
Copiar código
{
  "acessos": 3
}
✅ Pronto! Agora você tem:
Uma API serverless que conta acessos 🎯

Função Lambda com integração DynamoDB 🧠

Dados persistentes e atualizados a cada chamada 📊
![print1](https://github.com/user-attachments/assets/3b359af7-983c-4857-a050-c23f27632a35)
![print2](https://github.com/user-attachments/assets/9d548bcb-46e6-4309-a947-0c1f77a07705)
![print3](https://github.com/user-attachments/assets/a6437dbd-bf98-4d85-8225-d1939fb3c5f3)


