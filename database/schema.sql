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
