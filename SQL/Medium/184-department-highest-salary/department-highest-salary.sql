WITH RankedSalaries AS(
    SELECT
    e.Name AS Employee,
    e.Salary,
    e.departmentId,
    DENSE_RANK() OVER (
        PARTITION BY departmentId
        ORDER BY Salary DESC
    ) AS salary_rank
    FROM Employee AS e
)
SELECT d.Name AS Department, rs.Employee, rs.Salary
FROM RankedSalaries AS rs
JOIN Department AS d ON rs.departmentId = d.Id
WHERE rs.salary_rank = 1;