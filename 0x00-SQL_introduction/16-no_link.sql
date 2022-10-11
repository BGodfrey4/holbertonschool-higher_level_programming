-- lists all records of table second_table of the database hbtn_0c_0
-- lists all records in a table except rows without a name value
SELECT `score`, `name` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
