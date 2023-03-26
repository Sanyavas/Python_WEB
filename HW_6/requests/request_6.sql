-- Знайти список студентів у певній групі.

SELECT s.fullname AS student, g.name AS group
FROM students s
LEFT JOIN groups g ON g.id = s.group_id
WHERE g.id = 3
ORDER BY s.fullname;