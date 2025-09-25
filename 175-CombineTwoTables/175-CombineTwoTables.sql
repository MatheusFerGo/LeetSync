-- Last updated: 25/09/2025, 08:27:21
# Write your MySQL query statement below
SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;