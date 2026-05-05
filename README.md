# 🚀 AWS Smart Course Enrollment System

A fully serverless course enrollment web application built on AWS.  
Students can browse courses and enroll — all data is stored in **Amazon RDS (MySQL)** with a **JSON backup in S3**.

---

## 🌐 Live Website

Hosted on **Amazon S3** (Static Website Hosting)
LINK : http://novaedge-website-123.s3-website.ap-south-1.amazonaws.com/
---

## 🏗️ Architecture

```
Student (Browser)
       │
       ▼
  S3 Static Website (index.html)
       │
       ▼ HTTP POST
  API Gateway (REST API)
       │
       ▼
  Lambda Function (Python 3.12)
    ┌──┴──────────────┐
    ▼                 ▼
 RDS MySQL        S3 Bucket
(enrollments     (JSON backup
  table)          per student)
```

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| **Amazon S3** | Host the HTML website + store JSON backups |
| **Amazon RDS (MySQL)** | Store student enrollment records |
| **AWS Lambda** | Serverless backend logic (Python) |
| **Amazon API Gateway** | REST API endpoint for form submission |
| **AWS IAM** | Permissions and roles |

---

## 📋 Features

- 🎓 12 courses displayed with expandable details
- 📝 Enrollment form (First Name, Last Name, Course, Email, Mobile)
- ☁️ Data stored in MySQL database (RDS)
- 💾 JSON backup saved to S3 for every enrollment
- ✅ Success toast notification on form submit
- 📱 Fully responsive design

---

## 🗂️ Project Structure

```
AWS-Smart-Course-Enrollment-System/
├── index.html            # Frontend website (hosted on S3)
├── lambda_function.py    # AWS Lambda backend (Python 3.12)
└── README.md             # Project documentation
```

---

## 🛠️ Setup Guide

### Step 1 — S3 (Website Hosting)
1. Create S3 bucket (e.g. `novaedge-website-123`)
2. Enable **Static Website Hosting**
3. Upload `index.html`
4. Set bucket policy for public access
5. Note the **Website Endpoint URL**

### Step 2 — RDS (MySQL Database)
1. Create RDS MySQL instance (Free Tier)
2. Set **Public access → Yes**
3. Note the **Endpoint URL**
4. Connect via MySQL Workbench and run:

```sql
CREATE DATABASE novaedge_db;
USE novaedge_db;

CREATE TABLE enrollments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  course VARCHAR(100),
  email VARCHAR(150),
  mobile VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 3 — Lambda Function
1. Create Lambda function (Python 3.12)
2. Upload `lambda_function.py` with pymysql included in zip
3. Set Environment Variables:

| Key | Value |
|---|---|
| DB_HOST | your RDS endpoint |
| DB_USER | admin |
| DB_PASS | your password |
| DB_NAME | novaedge_db |
| BUCKET_NAME | your S3 bucket name |

4. Attach IAM policies: `AmazonS3FullAccess`, `AmazonRDSFullAccess`

### Step 4 — API Gateway
1. Create REST API
2. Create resource `/enroll`
3. Create POST method → connect to Lambda
4. Enable CORS
5. Deploy to stage `prod`
6. Note the **Invoke URL**

### Step 5 — Connect Frontend
In `index.html`, replace:
```javascript
var API_URL = 'https://YOUR_API_GATEWAY_URL/enroll';
```
with your actual API Gateway URL.

---

## 🧪 How to Test

1. Open your S3 website URL
2. Fill in the enrollment form
3. Click **Submit Enrollment**
4. Check RDS: `SELECT * FROM enrollments;`
5. Check S3 bucket → `enrollments/` folder for JSON backup

---

## 📊 Database Schema

```sql
CREATE TABLE enrollments (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  first_name  VARCHAR(100),
  last_name   VARCHAR(100),
  course      VARCHAR(100),
  email       VARCHAR(150),
  mobile      VARCHAR(20),
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔐 Security Notes

- RDS security group allows MySQL port 3306
- Lambda has IAM role with S3 and RDS access
- API Gateway has CORS enabled
- For production: restrict `0.0.0.0/0` to specific IPs

---

## 👨‍💻 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (single file)
- **Backend:** Python 3.12 (AWS Lambda)
- **Database:** MySQL 8.0 (Amazon RDS)
- **Cloud:** Amazon Web Services (AWS)

---

## 📸 Project Flow

```
User fills form → API Gateway → Lambda → RDS (saves row)
                                       → S3  (saves JSON)
                              ← success message shown
```

---

## 🎓 About

Built as a beginner AWS project to learn:
- Serverless architecture
- Cloud database management
- REST API design
- Static website hosting on AWS

