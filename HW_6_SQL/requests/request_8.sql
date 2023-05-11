-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT t.fullname as teacher, d."name" as discipline, ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
left join teachers t on t.id = d.teacher_id
WHERE t.id = 5
GROUP BY t.id, d.id;