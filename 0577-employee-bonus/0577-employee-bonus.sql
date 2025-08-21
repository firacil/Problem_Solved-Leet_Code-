# Write your MySQL query statement below
SELECT e.name as name, b.bonus as bonus from Employee e LEFT JOIN Bonus b ON(e.empId=b.empId)
WHERE bonus < 1000 OR b.bonus IS NULL