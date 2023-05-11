-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT gr.name AS group, d."name" as discipline, s.fullname AS student, max(g.date_of) as max_date, g.grade
FROM grades g
join disciplines d  on d.id = g.discipline_id
join students s on s.id = g.student_id
JOIN "groups" gr on gr.id = s.group_id
WHERE gr.id = 1 and d.id = 4
and g.date_of =
      (
	  SELECT MAX(date_of)
	  FROM grades g2
	  JOIN students s2 ON s2.id = g2.student_id
	  JOIN "groups" gr2  ON gr2.id = s2.group_id
	  WHERE g2.discipline_id = g.discipline_id AND gr2.id = gr.id
	  )
GROUP BY gr."name", d."name", s.fullname, g,grade, g.date_of
ORDER BY max_date desc;