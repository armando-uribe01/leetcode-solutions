SELECT x,y,z,
/* note that CASE is used instead of IF in order to achieve compatibility across SQL databases */
    CASE
        WHEN x + y > z AND x + z >y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM triangle;