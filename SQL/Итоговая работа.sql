9)Вычислите расстояние между аэропортами, связанными прямыми рейсами, сравните с допустимой максимальной дальностью перелетов  в самолетах, обслуживающих эти рейсы *
- Оператор RADIANS или использование sind/cosd
- CASE 

Соединяем таблицы flights, airports, aircrafts так как в них содержаться интересующие нас значения.
Выбираем нужные столбцы и расчитывает расстояние по указанной формуле:
d = arccos {sin(latitude_a)·sin(latitude_b) + cos(latitude_a)·cos(latitude_b)·cos(longitude_a - longitude_b)},
где latitude_a и latitude_b — широты, longitude_a,
longitude_b — долготы данных пунктов, d — расстояние между пунктами измеряется в радианах длиной дуги большого круга земного шара.
Расстояние между пунктами, измеряемое в километрах, определяется по формуле:
L = d·R, где R = 6371 км — средний радиус земного шара.
Затем с помощью оператора case выведем информацию о безопасности полета.Расчеты очень грубые и не отражают реальной ситуации,
так как для каждого рейса, для каждого самолета запас топлива различен и влияют такие факторы как погодные условия, высота полета,
нагруженность самолета и т.д. 
У самолетов совершающих полет, должно быть в запасе 15% процентов топлива на непредвиденные ситуации, мы же возьмем 15% от 
максимальной дальности перелета.
Если дальность перелета меньше 85% от максимальной дальности самолета, то отобразим что перелет безопасен,
если нет, то отобразим что это предельная нагрузка на самолет.

Минус 10 баллов.
В результате должен быть список маршрутов, а не перелетов.

select distinct
       a.airport_name as departure_airport_name,
       a1.airport_name as arrival_airport_name,
       a2.aircraft_code,
       a2.model,
       a2."range",
       round((acos(sind(a.latitude) * sind(a1.latitude) 
       + cosd(a.latitude) * cosd(a1.latitude) 
       * cosd(a.longitude - a1.longitude)) * 6371)::dec, 2)  as distance,
       case 
       	when a2."range"*100/(round((acos(sind(a.latitude) * sind(a1.latitude) 
       + cosd(a.latitude) * cosd(a1.latitude) 
       * cosd(a.longitude - a1.longitude)) * 6371)::dec, 2)) > '85' then 'безопасно'
       else 'предельная нагрузка'
       end as flight_safety
from flights f
inner join airports a on f.departure_airport = a.airport_code 
inner join airports a1 on f.arrival_airport = a1.airport_code
inner join aircrafts a2 on f.aircraft_code = a2.aircraft_code


7)Были ли города, в которые можно  добраться бизнес - классом дешевле, чем эконом-классом в рамках перелета?
- CTE

Минус 10 баллов.
Не логично сравнивать минимальный эконом с минимальным бизнесом.


with econom as (
           select
           flight_id,
           fare_conditions,
           amount as econom_amount
           from ticket_flights
           where fare_conditions = 'Economy'),
     business as (
           select
           flight_id,
           fare_conditions,
           amount as business_amount
           from ticket_flights
           where fare_conditions = 'Business')
select distinct
       f.flight_id,
       arrival_airport,
       a.city,
       e.econom_amount,
       b.business_amount
from flights f
join airports a on a.airport_code = f.arrival_airport
join econom e on e.flight_id = f.flight_id
join business b on b.flight_id = f.flight_id
where b.business_amount < e.econom_amount


6 Найдите процентное соотношение перелетов по типам самолетов от общего количества.
- Подзапрос или окно
- Оператор ROUND

Минус 15 баллов.
Потеряли половину данных. 

with cte as (select aircraft_code,
      count(flight_id) as aircraft_flight,
      (select count(flight_id) from flights) as all_flight
from flights
group by aircraft_code)
select a.model,
       c.all_flight,
       c.aircraft_flight,
       round((c.aircraft_flight::dec*100/c.all_flight::dec),2) as percent_flight
from cte c
inner join aircrafts a on a.aircraft_code = c.aircraft_code






















