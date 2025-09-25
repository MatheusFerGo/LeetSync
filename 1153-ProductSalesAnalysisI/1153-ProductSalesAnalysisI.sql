-- Last updated: 25/09/2025, 08:27:17
SELECT p.product_name, s.year, s.price FROM Sales as s, Product as p
WHERE p.product_id = s.product_id