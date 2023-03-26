-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT s.fullname AS student, g.name AS group, g2.grade, d."name" as discipline
FROM students s
left join grades g2 on g2.student_id = g2.grade
LEFT JOIN groups g ON g.id = s.group_id
left join disciplines d on d.id = g2.discipline_id
WHERE g.id = 1 and d.id = 4
ORDER BY s.fullname;