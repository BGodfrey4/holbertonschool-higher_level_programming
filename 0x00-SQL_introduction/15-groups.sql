-- lists records with same score in the table second_table
-- groups rows together having the same scores and displays the number of occurrences
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC
