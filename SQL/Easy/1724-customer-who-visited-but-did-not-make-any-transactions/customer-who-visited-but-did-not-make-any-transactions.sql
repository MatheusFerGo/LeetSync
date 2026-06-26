SELECT 
    v.customer_id, 
    COUNT(v.visit_id) AS count_no_trans
FROM 
    Visits AS v
-- Juntamos todas as visitas com as transações
LEFT JOIN 
    Transactions AS t 
ON 
    v.visit_id = t.visit_id
WHERE 
    -- Se o ID da transação for nulo, significa que a visita não gerou compra
    t.transaction_id IS NULL
GROUP BY 
    v.customer_id;