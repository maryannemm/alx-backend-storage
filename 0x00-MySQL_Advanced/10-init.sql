-- Initial data setup for task 10
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a INT DEFAULT 0,
    b INT DEFAULT 0
);

INSERT INTO numbers (a, b) VALUES 
(10, 2), 
(4, 5), 
(2, 3), 
(6, 3), 
(7, 0), 
(6, 8);

