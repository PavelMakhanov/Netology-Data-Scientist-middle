--=============== МОДУЛЬ 4. УГЛУБЛЕНИЕ В SQL =======================================
--= ПОМНИТЕ, ЧТО НЕОБХОДИМО УСТАНОВИТЬ ВЕРНОЕ СОЕДИНЕНИЕ И ВЫБРАТЬ СХЕМУ PUBLIC===========
SET search_path TO public;

--======== ОСНОВНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--База данных: если подключение к облачной базе, то создаёте новую схему с префиксом в --виде фамилии, название должно быть на латинице в нижнем регистре и таблицы создаете --в этой новой схеме, если подключение к локальному серверу, то создаёте новую схему и --в ней создаёте таблицы.

--Спроектируйте базу данных, содержащую три справочника:
--· язык (английский, французский и т. п.);
--· народность (славяне, англосаксы и т. п.);
--· страны (Россия, Германия и т. п.).
--Две таблицы со связями: язык-народность и народность-страна, отношения многие ко многим. Пример таблицы со связями — film_actor.
--Требования к таблицам-справочникам:
--· наличие ограничений первичных ключей.
--· идентификатору сущности должен присваиваться автоинкрементом;
--· наименования сущностей не должны содержать null-значения, не должны допускаться --дубликаты в названиях сущностей.
--Требования к таблицам со связями:
--· наличие ограничений первичных и внешних ключей.

--В качестве ответа на задание пришлите запросы создания таблиц и запросы по --добавлению в каждую таблицу по 5 строк с данными.
 
--СОЗДАНИЕ ТАБЛИЦЫ ЯЗЫКИ

create table "language"(
     language_id serial primary key,
     "name" varchar (50) unique not null)


--ВНЕСЕНИЕ ДАННЫХ В ТАБЛИЦУ ЯЗЫКИ

insert into "language"("name")
values ('English'),('French'),('Russian'),('German'),('Italian')


--СОЗДАНИЕ ТАБЛИЦЫ НАРОДНОСТИ

create table nationality (
     nationality_id serial primary key,
     "name" varchar (50) unique not null) 


--ВНЕСЕНИЕ ДАННЫХ В ТАБЛИЦУ НАРОДНОСТИ

insert into nationality("name")
values ('Anglo - Saxons'),('French'),('Russian'),('German'),('Italian')


--СОЗДАНИЕ ТАБЛИЦЫ СТРАНЫ

create table countries (
     countries_id serial primary key,
     "name" varchar (50) unique not null)


--ВНЕСЕНИЕ ДАННЫХ В ТАБЛИЦУ СТРАНЫ

insert into countries("name")
values ('Great Britain'),('France'),('Russia'),('Germany'),('Italy')


--СОЗДАНИЕ ПЕРВОЙ ТАБЛИЦЫ СО СВЯЗЯМИ

CREATE TABLE language_nationality (
	language_id int2 NOT NULL,
	nationality_id int2 NOT NULL,
	last_update timestamp NOT NULL DEFAULT now(),
	CONSTRAINT language_nationality_pkey PRIMARY KEY (language_id, nationality_id),
	CONSTRAINT language_nationality_language_id_fkey FOREIGN KEY (language_id) REFERENCES "language"(language_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	CONSTRAINT language_nationality_nationality_id_fkey FOREIGN KEY (nationality_id) REFERENCES nationality(nationality_id) ON DELETE RESTRICT ON UPDATE CASCADE);


--ВНЕСЕНИЕ ДАННЫХ В ТАБЛИЦУ СО СВЯЗЯМИ

insert into language_nationality(language_id,nationality_id)
SELECT language_id,nationality_id FROM "language", nationality
where language_id = nationality_id


--СОЗДАНИЕ ВТОРОЙ ТАБЛИЦЫ СО СВЯЗЯМИ
CREATE TABLE nationality_countries (
	countries_id int2 NOT NULL,
	nationality_id int2 NOT NULL,
	last_update timestamp NOT NULL DEFAULT now(),
	CONSTRAINT nationality_countries_pkey PRIMARY KEY (countries_id, nationality_id),
	CONSTRAINT language_nationality_countries_id_fkey FOREIGN KEY (countries_id) REFERENCES countries(countries_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	CONSTRAINT language_nationality_nationality_id_fkey FOREIGN KEY (nationality_id) REFERENCES nationality(nationality_id) ON DELETE RESTRICT ON UPDATE CASCADE);


--ВНЕСЕНИЕ ДАННЫХ В ТАБЛИЦУ СО СВЯЗЯМИ

insert into nationality_countries(countries_id,nationality_id)
SELECT countries_id,nationality_id FROM countries, nationality
where countries_id = nationality_id

--======== ДОПОЛНИТЕЛЬНАЯ ЧАСТЬ ==============


--ЗАДАНИЕ №1 
--Создайте новую таблицу film_new со следующими полями:
--·   	film_name - название фильма - тип данных varchar(255) и ограничение not null
--·   	film_year - год выпуска фильма - тип данных integer, условие, что значение должно быть больше 0
--·   	film_rental_rate - стоимость аренды фильма - тип данных numeric(4,2), значение по умолчанию 0.99
--·   	film_duration - длительность фильма в минутах - тип данных integer, ограничение not null и условие, что значение должно быть больше 0
--Если работаете в облачной базе, то перед названием таблицы задайте наименование вашей схемы.



--ЗАДАНИЕ №2 
--Заполните таблицу film_new данными с помощью SQL-запроса, где колонкам соответствуют массивы данных:
--·       film_name - array['The Shawshank Redemption', 'The Green Mile', 'Back to the Future', 'Forrest Gump', 'Schindlers List']
--·       film_year - array[1994, 1999, 1985, 1994, 1993]
--·       film_rental_rate - array[2.99, 0.99, 1.99, 2.99, 3.99]
--·   	  film_duration - array[142, 189, 116, 142, 195]



--ЗАДАНИЕ №3
--Обновите стоимость аренды фильмов в таблице film_new с учетом информации, 
--что стоимость аренды всех фильмов поднялась на 1.41



--ЗАДАНИЕ №4
--Фильм с названием "Back to the Future" был снят с аренды, 
--удалите строку с этим фильмом из таблицы film_new



--ЗАДАНИЕ №5
--Добавьте в таблицу film_new запись о любом другом новом фильме



--ЗАДАНИЕ №6
--Напишите SQL-запрос, который выведет все колонки из таблицы film_new, 
--а также новую вычисляемую колонку "длительность фильма в часах", округлённую до десятых



--ЗАДАНИЕ №7 
--Удалите таблицу film_new