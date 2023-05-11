-- Середній бал, який певний викладач ставить певному студентові.

SELECT t.fullname as teacher, s.fullname AS student, d."name" as discipline, ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
left join disciplines d  on d.id = g.discipline_id
left join students s on s.id = g.student_id
LEFT JOIN teachers t on t.id = d.teacher_id
LEFT JOIN grades g2 on g2.student_id = g2.discipline_id
WHERE s.id = 5 and t.id = 2
GROUP BY t.fullname, s.fullname, d."name"
ORDER BY avg_grade DESC;