-- https://programmers.co.kr/learn/courses/30/lessons/59047

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
WHERE NAME LIKE "%el%" and ANIMAL_TYPE = "Dog" 
ORDER BY NAME ASC;