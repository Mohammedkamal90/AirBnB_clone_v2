-- setup_mysql_dev.sql
-- Create or use hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create or use hbnb_dev user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant privileges to hbnb_dev user on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT privilege to hbnb_dev user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
