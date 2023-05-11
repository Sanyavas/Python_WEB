-- Список курсів, які певному студенту читає певний викладач.

SELECT s.fullname AS student, t.fullname as teacher, d."name" as discipline
FROM grades g
left join disciplines d  on d.id = g.discipline_id
left join students s on s.id = g.student_id
LEFT JOIN teachers t on t.id = d.teacher_id
WHERE s.id = 2 and t.id = 1
GROUP BY d."name", t.fullname, s.fullname;

