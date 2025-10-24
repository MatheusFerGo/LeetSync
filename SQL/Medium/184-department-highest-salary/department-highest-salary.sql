SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary FROM Employee AS e
LEFT JOIN Department as d ON d.id = e.departmentId
WHERE
    (e.departmentId, e.Salary) IN (
        SELECT
            departmentId,
            MAX(Salary)
        FROM
            Employee
        GROUP BY
            departmentId
    );