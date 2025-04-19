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