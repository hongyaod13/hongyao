import hw_a,hw_b;
SELECT b.sn 
FROM TABLE hw_b b
RIGHT JOIN TABLE hw_a a
ON a.Key=b.Key
WHERE A.Key IS NULL;
