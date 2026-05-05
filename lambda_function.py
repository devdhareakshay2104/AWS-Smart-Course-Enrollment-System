import json
import boto3
import pymysql
import os
from datetime import datetime

def lambda_handler(event, context):
    body = json.loads(event['body'])

    # Connect to RDS
    conn = pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        database=os.environ['DB_NAME']
    )

    cursor = conn.cursor()

    # Insert into table
    cursor.execute(
        "INSERT INTO enrollments (first_name,last_name,course,email,mobile) VALUES (%s,%s,%s,%s,%s)",
        (
            body['first_name'],
            body['last_name'],
            body['course'],
            body['email'],
            body['mobile']
        )
    )

    conn.commit()
    conn.close()

    # Save JSON backup to S3
    s3 = boto3.client('s3')
    filename = f"enrollments/{body['email']}_{datetime.now().isoformat()}.json"

    s3.put_object(
        Bucket=os.environ['BUCKET_NAME'],
        Key=filename,
        Body=json.dumps(body)
    )

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'message': 'Enrollment successful'})
    }