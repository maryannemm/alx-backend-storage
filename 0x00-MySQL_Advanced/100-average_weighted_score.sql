-- Task 12: Average weighted score
-- This script creates a stored procedure 'ComputeAverageWeightedScoreForUser' that calculates
-- the average weighted score for a single user and updates their average_score in the 'users' table.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_score FLOAT;

    -- Calculate the weighted average score for the user
    SELECT SUM(score * weight) / SUM(weight) INTO weighted_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Update the user's average score
    UPDATE users
    SET average_score = weighted_score
    WHERE id = user_id;
END //

DELIMITER ;

