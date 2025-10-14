SELECT e.name AS Employee FROM Employee AS e
JOIN Employee as M on e.managerId = m.id
WHERE e.salary > m.salary;