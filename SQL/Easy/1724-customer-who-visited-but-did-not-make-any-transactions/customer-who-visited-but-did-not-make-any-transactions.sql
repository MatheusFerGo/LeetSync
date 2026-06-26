SELECT v.customer_id, COUNT(v.visit_id) as count_no_trans
FROM Visits as v
WHERE v.visit_id NOT IN (SELECT t.visit_id 
                        FROM Transactions as t)
GROUP BY v.customer_id