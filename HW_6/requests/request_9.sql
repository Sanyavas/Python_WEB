-- Знайти список курсів, які відвідує студент.

SELECT s.fullname as student, d."name" as discipline
FROM grades g
join disciplines d on d.id = g.discipline_id
left join students s  on s.id = g.student_id
where s.id = 2
GROUP BY s.id, d.id