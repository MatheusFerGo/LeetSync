SELECT id,
    CASE
        WHEN p_id IS NULL THEN 'Root'

        WHEN id IN(
            SELECT DISTINCT p_id
            FROM Tree
            WHERE id IS NOT NULL
        )THEN 'Inner'

        ELSE 'Leaf'
    END AS type
FROM Tree;