-- https://programmers.co.kr/learn/courses/30/lessons/59411

SELECT a.ANIMAL_ID, a.NAME FROM ANIMAL_INS as a, ANIMAL_OUTS as b
WHERE a.ANIMAL_ID = b.ANIMAL_ID
ORDER BY b.DATETIME - a.DATETIME DESC
LIMIT 2;