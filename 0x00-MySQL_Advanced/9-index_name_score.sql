-- Task 9: Optimize search by name and score
-- Create an index on the first letter of the name and score

CREATE INDEX idx_name_first_score ON names (name(1), score);

