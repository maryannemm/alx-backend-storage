-- Task 0: We are all unique!
-- This script creates a table `users` with the specified attributes
-- The email column is unique

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

