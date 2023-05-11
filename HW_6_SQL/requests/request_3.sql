-- Знайти середній бал у групах з певного предмета.

SELECT gr.name as group, d.name as discipline , ROUND(avg(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
left join "groups" gr on gr.id = s.group_id
WHERE d.id = 1
GROUP BY gr.id, d.id
ORDER BY avg_grade DESC