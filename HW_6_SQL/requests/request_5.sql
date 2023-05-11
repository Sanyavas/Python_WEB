-- Знайти які курси читає певний викладач.

SELECT t.fullname as teacher, d.name as discipline
FROM disciplines d
left join teachers t on t.id = d.teacher_id
where t.id = 2
GROUP BY t.id, d.id;