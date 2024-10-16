-- Task 4: Buy buy buy
-- This script creates a trigger to decrease the quantity of items after adding a new order

DELIMITER //
CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;

