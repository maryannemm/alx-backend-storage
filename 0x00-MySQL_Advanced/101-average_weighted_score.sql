-- Task 13: Average weighted score for all
-- This script creates a stored procedure 'ComputeAverageWeightedScoreForUsers' that calculates
-- the average weighted score for all users and updates their average_score in the 'users' table.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE done INT DEFAULT 0;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open the cursor to loop through all users
    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Call procedure for individual user
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;

