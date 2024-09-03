SELECT 
countries.country_name,
actors.first_name,
actors.last_name
FROM
countries
FULL JOIN
actors ON countries.country_id = actors.actor_id;