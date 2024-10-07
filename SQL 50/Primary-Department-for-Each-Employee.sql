SELECT 
    employee_id, 
    department_id 
FROM 
    employee 
WHERE 
    primary_flag = 'Y' OR 
    (primary_flag = 'N' AND employee_id NOT IN (
        SELECT employee_id 
        FROM employee 
        WHERE primary_flag = 'Y'
    ));    