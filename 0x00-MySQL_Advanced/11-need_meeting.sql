-- Task 11: No table for a meeting
-- This script creates a view 'need_meeting' that lists students whose score is under 80,
-- and who either have no last meeting or whose last meeting was over a month ago.

CREATE OR REPLACE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));

