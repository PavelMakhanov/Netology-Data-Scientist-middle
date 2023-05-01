--=============== МОДУЛЬ 3. ОСНОВЫ SQL =======================================
--= ПОМНИТЕ, ЧТО НЕОБХОДИМО УСТАНОВИТЬ ВЕРНОЕ СОЕДИНЕНИЕ И ВЫБРАТЬ СХЕМУ PUBLIC===========
SET search_path TO public;

--======== ОСНОВНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--Выведите для каждого покупателя его адрес проживания, 
--город и страну проживания.

select 
     concat(pok.last_name,' ',pok.first_name) as Customer_name,
     ad.address,
     cit.city,
     cou.country
from address ad
inner join customer pok on ad.address_id = pok.address_id
inner join city cit on cit.city_id = ad.city_id
inner join country cou on cit.country_id = cou.country_id



--ЗАДАНИЕ №2
--С помощью SQL-запроса посчитайте для каждого магазина количество его покупателей.

select 
   store_id as "ID магазина",
   count(customer_id) as "Количество покупателей"
from customer
group by store_id



--Доработайте запрос и выведите только те магазины, 
--у которых количество покупателей больше 300-от.
--Для решения используйте фильтрацию по сгруппированным строкам 
--с использованием функции агрегации.

select 
   store_id as "ID магазина",
   count(customer_id) as "Количество покупателей"
from customer
group by store_id
having count(customer_id) > 300




-- Доработайте запрос, добавив в него информацию о городе магазина, 
--а также фамилию и имя продавца, который работает в этом магазине.

select
    s.store_id as ID_магазина,
    count(cus.customer_id) as Количество_покупателей,
    c.city as Город,
    concat(st.last_name,' ',st.first_name) as Имя_сотрудника
from store s
join customer cus on cus.store_id = s.store_id
join address ad on ad.address_id = s.address_id
join city c on ad.city_id = c.city_id
join staff st on s.store_id = st.store_id
group by s.store_id, c.city,st.staff_id 
having count(customer_id) > 300



--ЗАДАНИЕ №3
--Выведите ТОП-5 покупателей, 
--которые взяли в аренду за всё время наибольшее количество фильмов

select 
    concat(cus.last_name,' ',cus.first_name) as Фамилия_и_имя_Покупателя,
    count(i.film_id) as Количество_фильмов
    from customer cus
inner join rental r on cus.customer_id = r.customer_id
inner join inventory i on i.inventory_id = r.inventory_id
group by Фамилия_и_имя_Покупателя
order by Количество_фильмов desc
limit 5




--ЗАДАНИЕ №4
--Посчитайте для каждого покупателя 4 аналитических показателя:
--  1. количество фильмов, которые он взял в аренду
--  2. общую стоимость платежей за аренду всех фильмов (значение округлите до целого числа)
--  3. минимальное значение платежа за аренду фильма
--  4. максимальное значение платежа за аренду фильма

select 
    concat(cus.last_name,' ',cus.first_name) as Фамилия_и_имя_Покупателя,
    count(r.rental_id)as Количество_фильмов,
    round(sum(p.amount)) as Общая_стоимость_платежей,
    min(p.amount) as Минимальная_стоимость_платежа,
    max(p.amount) as Максимальная_стоимость_платежа
    from customer cus
inner join rental r on cus.customer_id = r.customer_id
inner join inventory i on i.inventory_id = r.inventory_id
inner join payment p on cus.customer_id = p.customer_id and p.rental_id = r.rental_id
group by Фамилия_и_имя_Покупателя



--ЗАДАНИЕ №5
--Используя данные из таблицы городов составьте одним запросом всевозможные пары городов таким образом,
 --чтобы в результате не было пар с одинаковыми названиями городов. 
 --Для решения необходимо использовать декартово произведение.

select 
   a1.city,
   a2.city
from city a1
cross join city a2
where a1.city != a2.city
 


--ЗАДАНИЕ №6
--Используя данные из таблицы rental о дате выдачи фильма в аренду (поле rental_date)
--и дате возврата фильма (поле return_date), 
--вычислите для каждого покупателя среднее количество дней, за которые покупатель возвращает фильмы.
 
select 
   customer_id as ID_покупателя,
   avg(date(return_date)-date(rental_date)) as Среднее_количество_дней_возврата
from rental
group by customer_id



--======== ДОПОЛНИТЕЛЬНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--Посчитайте для каждого фильма сколько раз его брали в аренду и значение общей стоимости аренды фильма за всё время.

select 
   f.title as Название_фильма,
   f.rating as Рейтинг,
   c."name" as Жанр,
   f.release_year as Год_выпуска,
   l."name" as Язык,
   count(r.rental_id) as Количество_аренд,
   sum(p.amount) as Общая_стоимость_платежей
from film f 
inner join film_category fc on f.film_id = fc.film_id
inner join category c on c.category_id = fc.category_id
inner join "language" l on l.language_id = f.language_id
inner join inventory i on i.film_id = f.film_id
inner join rental r on i.inventory_id = r.inventory_id
inner join payment p on p.customer_id = r.customer_id and p.rental_id = r.rental_id
group by f.title,f.rating,c."name",f.release_year,l."name"



--ЗАДАНИЕ №2
--Доработайте запрос из предыдущего задания и выведите с помощью запроса фильмы, которые ни разу не брали в аренду.

select 
   f.title as Название_фильма,
   f.rating as Рейтинг,
   c."name" as Жанр,
   f.release_year as Год_выпуска,
   l."name" as Язык,
   count(r.rental_id) as Количество_аренд,
   sum(p.amount) as Общая_стоимость_платежей
from film f 
inner join film_category fc on f.film_id = fc.film_id
inner join category c on c.category_id = fc.category_id
inner join "language" l on l.language_id = f.language_id
left join inventory i on i.film_id = f.film_id
left join rental r on i.inventory_id = r.inventory_id
left join payment p on p.customer_id = r.customer_id and p.rental_id = r.rental_id
group by f.title,f.rating,c."name",f.release_year,l."name"
having count(r.rental_id) = 0



--ЗАДАНИЕ №3
--Посчитайте количество продаж, выполненных каждым продавцом. Добавьте вычисляемую колонку "Премия".
--Если количество продаж превышает 7300, то значение в колонке будет "Да", иначе должно быть значение "Нет".

select
   s.staff_id,
   count(p.payment_id) as Количество_продаж,
   case 
   	when count(p.payment_id) > 7300 then 'ДА'
   	else 'НЕТ'
   end
from staff s
inner join payment p on p.staff_id = s.staff_id
group by s.staff_id






