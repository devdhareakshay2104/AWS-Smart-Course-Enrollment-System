# Setup Guide

1. Create S3 bucket → enable static website hosting → upload index.html
2. Create RDS MySQL → run database/schema.sql
3. Create Lambda → upload lambda_function.py → add env vars
4. Create API Gateway → POST /enroll → link Lambda → deploy prod stage
5. Update index.html with your API Gateway URL
