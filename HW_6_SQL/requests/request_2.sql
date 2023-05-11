-- Знайти студента із найвищим середнім балом з певного предмета.

SELECT d.name as discipline, s.fullname as student, ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id IN (1)
GROUP BY s.id, d.id
ORDER BY avg_grade DESC
LIMIT 1;