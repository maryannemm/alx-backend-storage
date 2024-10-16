-- Task 10: Safe divide
-- This script creates a function SafeDiv that divides the first argument by the second.
-- If the second argument is 0, it returns 0 instead of NULL.

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ;

