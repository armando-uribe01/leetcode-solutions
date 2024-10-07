WITH cte AS (
    SELECT 
        num,
        id,
        LEAD(id, 1) OVER (PARTITION BY num ORDER BY id) AS next_id_1,
        LEAD(id, 2) OVER (PARTITION BY num ORDER BY id) AS next_id_2
    FROM logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM cte
WHERE 
    next_id_1 = id + 1 
    AND next_id_2 = id + 2;