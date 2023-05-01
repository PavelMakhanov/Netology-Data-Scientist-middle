--=============== МОДУЛЬ 5. РАБОТА С POSTGRESQL =======================================
--= ПОМНИТЕ, ЧТО НЕОБХОДИМО УСТАНОВИТЬ ВЕРНОЕ СОЕДИНЕНИЕ И ВЫБРАТЬ СХЕМУ PUBLIC===========
SET search_path TO public;

--======== ОСНОВНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--Сделайте запрос к таблице payment и с помощью оконных функций добавьте вычисляемые колонки согласно условиям:
--Пронумеруйте все платежи от 1 до N по дате
--Пронумеруйте платежи для каждого покупателя, сортировка платежей должна быть по дате
--Посчитайте нарастающим итогом сумму всех платежей для каждого покупателя, сортировка должна 
--быть сперва по дате платежа, а затем по сумме платежа от наименьшей к большей
--Пронумеруйте платежи для каждого покупателя по стоимости платежа от наибольших к меньшим 
--так, чтобы платежи с одинаковым значением имели одинаковое значение номера.
--Можно составить на каждый пункт отдельный SQL-запрос, а можно объединить все колонки в одном запросе.

select  customer_id, payment_id,payment_date,
row_number() over(order by payment_date)
from payment

select  customer_id, payment_id,payment_date,
row_number() over(partition by customer_id order by payment_date)
from payment
order by payment_date

select  customer_id, payment_id,payment_date,
sum(amount) over(partition by customer_id order by payment_date,amount)
from payment


select  customer_id, payment_id,payment_date, amount,
dense_rank() over(partition by customer_id order by amount desc) 
from payment



--ЗАДАНИЕ №2
--С помощью оконной функции выведите для каждого покупателя стоимость платежа и стоимость 
--платежа из предыдущей строки со значением по умолчанию 0.0 с сортировкой по дате.

select customer_id, payment_id, payment_date, amount,
 	lag(amount,1,0) over (partition by customer_id order by payment_date) as last_amount
 from payment 
 order by customer_id



--ЗАДАНИЕ №3
--С помощью оконной функции определите, на сколько каждый следующий платеж покупателя больше или меньше текущего.

select customer_id, payment_id, payment_date, amount,
  amount - lead(amount,1,0) over (partition by customer_id  order by payment_date, customer_id) as difference
from payment




--ЗАДАНИЕ №4
--С помощью оконной функции для каждого покупателя выведите данные о его последней оплате аренды.

with last_peyment as (
  select
   *, max (payment_date) over (partition by customer_id) as max_date
  from payment
)
select customer_id, payment_id , amount
from last_peyment
where
  payment_date = max_date



--======== ДОПОЛНИТЕЛЬНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--С помощью оконной функции выведите для каждого сотрудника сумму продаж за август 2005 года 
--с нарастающим итогом по каждому сотруднику и по каждой дате продажи (без учёта времени) 
--с сортировкой по дате.

select staff_id, payment_date,sum_amount,amount
from (select 
        staff_id,
        payment_date::date,
        sum(amount) over (partition by staff_id,payment_date::date order by payment_date::date) as sum_amount,
        sum(amount) over (partition by payment_date::date order by payment_date::date) as amount
from payment
where payment_date >= '2005-08-01 00:00:00.000' and payment_date < '2005-09-01 00:00:00.000') as p
group by staff_id, payment_date,sum_amount,amount
order by staff_id, payment_date




--ЗАДАНИЕ №2
--20 августа 2005 года в магазинах проходила акция: покупатель каждого сотого платежа получал
--дополнительную скидку на следующую аренду. С помощью оконной функции выведите всех покупателей,
--которые в день проведения акции получили скидку

select customer_id,
       payment_date,
       payment_number
from
       (select 
       customer_id,
       payment_date,
       row_number() over (order by payment_date) as payment_number
from payment
where payment_date::date = '2005-08-20 00:00:00.000') as c
where payment_number%100=0




--ЗАДАНИЕ №3
--Для каждой страны определите и выведите одним SQL-запросом покупателей, которые попадают под условия:
-- 1. покупатель, арендовавший наибольшее количество фильмов
-- 2. покупатель, арендовавший фильмов на самую большую сумму
-- 3. покупатель, который последним арендовал фильм






