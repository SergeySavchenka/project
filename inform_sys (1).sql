-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 04 2023 г., 21:30
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `inform_sys`
--

-- --------------------------------------------------------

--
-- Структура таблицы `auto`
--

CREATE TABLE `auto` (
  `auto_id` int NOT NULL,
  `mark` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `release_year` int DEFAULT NULL,
  `state_number` varchar(15) DEFAULT NULL,
  `vin` varchar(17) DEFAULT NULL,
  `fuel_type` varchar(20) DEFAULT NULL,
  `engine_volume` int DEFAULT NULL,
  `mileage` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `auto`
--

INSERT INTO `auto` (`auto_id`, `mark`, `model`, `release_year`, `state_number`, `vin`, `fuel_type`, `engine_volume`, `mileage`) VALUES
(1, 'volvo', 's3', 2009, 'r231ds', 'hf821kg51msh1087s', 'gas', 650, 120890),
(2, 'mercedes', 'amg63', 2013, 'a112mg', 'asdfghj158kl01ngb', 'petrol', 700, 220981);

-- --------------------------------------------------------

--
-- Структура таблицы `driver`
--

CREATE TABLE `driver` (
  `driver_id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `female` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `last_med_exam_date` date DEFAULT NULL,
  `drivers_license_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `driver`
--

INSERT INTO `driver` (`driver_id`, `name`, `female`, `birth_date`, `last_med_exam_date`, `drivers_license_number`) VALUES
(1, 'Никита', 'Голубятников', '2005-04-04', '2023-11-20', '210-420'),
(2, 'Андрей', 'Рогов', '2005-10-09', '2023-08-24', '423-298');

-- --------------------------------------------------------

--
-- Структура таблицы `routs`
--

CREATE TABLE `routs` (
  `rout_id` int NOT NULL,
  `auto_id` int DEFAULT NULL,
  `driver_id` int DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  `arrival_date` date DEFAULT NULL,
  `distance` int DEFAULT NULL,
  `destination` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `routs`
--

INSERT INTO `routs` (`rout_id`, `auto_id`, `driver_id`, `departure_date`, `arrival_date`, `distance`, `destination`) VALUES
(1, 2, 1, '2023-10-15', '2023-11-07', 670, 'Moscow'),
(2, 1, 2, '2023-01-23', '2023-02-01', 2100, 'Novorossiysk'),
(3, 1, 1, '2023-10-10', '2023-11-29', 1200, 'Minsk');

-- --------------------------------------------------------

--
-- Структура таблицы `technical_service`
--

CREATE TABLE `technical_service` (
  `service_id` int NOT NULL,
  `auto_id` int DEFAULT NULL,
  `service_date` date DEFAULT NULL,
  `service_type` varchar(50) DEFAULT NULL,
  `mileage` int DEFAULT NULL,
  `cost` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `technical_service`
--

INSERT INTO `technical_service` (`service_id`, `auto_id`, `service_date`, `service_type`, `mileage`, `cost`) VALUES
(1, 2, '2022-09-15', 'oil change', 1005, '12000.00'),
(2, 1, '2021-05-19', 'wheel change', 3000, '45000.00');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `auto`
--
ALTER TABLE `auto`
  ADD PRIMARY KEY (`auto_id`);

--
-- Индексы таблицы `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`driver_id`);

--
-- Индексы таблицы `routs`
--
ALTER TABLE `routs`
  ADD PRIMARY KEY (`rout_id`),
  ADD KEY `auto_id` (`auto_id`),
  ADD KEY `driver_id` (`driver_id`);

--
-- Индексы таблицы `technical_service`
--
ALTER TABLE `technical_service`
  ADD PRIMARY KEY (`service_id`),
  ADD KEY `auto_id` (`auto_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `auto`
--
ALTER TABLE `auto`
  MODIFY `auto_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `driver`
--
ALTER TABLE `driver`
  MODIFY `driver_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `routs`
--
ALTER TABLE `routs`
  MODIFY `rout_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `technical_service`
--
ALTER TABLE `technical_service`
  MODIFY `service_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `routs`
--
ALTER TABLE `routs`
  ADD CONSTRAINT `routs_ibfk_1` FOREIGN KEY (`auto_id`) REFERENCES `auto` (`auto_id`),
  ADD CONSTRAINT `routs_ibfk_2` FOREIGN KEY (`driver_id`) REFERENCES `driver` (`driver_id`);

--
-- Ограничения внешнего ключа таблицы `technical_service`
--
ALTER TABLE `technical_service`
  ADD CONSTRAINT `technical_service_ibfk_1` FOREIGN KEY (`auto_id`) REFERENCES `auto` (`auto_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
