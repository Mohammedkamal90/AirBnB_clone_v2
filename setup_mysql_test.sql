-- setup mysql_test.sql
-- Create or use the hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create or use the hbnb_test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant privileges to the hbnb_test user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege to the hbnb_test user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
