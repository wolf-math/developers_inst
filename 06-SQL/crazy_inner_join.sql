select payment.amount, film.title 
from payment
INNER JOIN rental
ON payment.rental_id = rental.rental_id
INNER JOIN inventory
ON rental.inventory_id = inventory.inventory_id
inner join film
on inventory.film_id = film.film_id
where rental.return_date is null
order by amount desc
limit 30
-- select * from rental where rental_id=14763;
-- select * from inventory where inventory_id = 1480;
-- select * from film where film_id = 324;