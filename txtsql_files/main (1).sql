-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2023 at 10:21 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `main`
--

-- --------------------------------------------------------

--
-- Table structure for table `authentication`
--

CREATE TABLE `authentication` (
  `id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_pass` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `cust_state` varchar(20) NOT NULL,
  `birthday` date NOT NULL,
  `points` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `email_id`, `cust_state`, `birthday`, `points`) VALUES
(1, 'Aditya', 'adityahakani29@gmail.com', 'Mumbai', '2023-05-15', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `fest_india`
--

CREATE TABLE `fest_india` (
  `id` int(11) NOT NULL,
  `fest_name` varchar(50) NOT NULL,
  `fest_date` date NOT NULL,
  `locality` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fest_india`
--

INSERT INTO `fest_india` (`id`, `fest_name`, `fest_date`, `locality`) VALUES
(1, 'Makar Sankranti', '2023-01-14', 'India'),
(2, 'Pongal', '2023-01-14', 'India'),
(3, 'Vasant Panchami', '2023-01-26', 'India'),
(4, 'Republic Day', '2023-01-26', 'India'),
(5, 'Maha Shivaratri', '2023-02-18', 'India'),
(6, 'Holi', '2023-03-08', 'Mumbai'),
(7, 'Ram Navmi', '2023-03-30', 'India'),
(8, 'Eid al fitr', '2023-04-22', 'India'),
(9, 'Janmashtmi', '2023-08-06', 'India'),
(10, 'Independance Day', '2023-08-15', 'India'),
(11, 'Raksha Bandhan', '2023-08-30', 'India'),
(12, 'Ganesh Chaturthi', '2023-09-19', 'India'),
(13, 'Navratri', '2023-06-18', 'Gujarat'),
(14, 'Dussehra', '2023-10-24', 'India'),
(15, 'Diwali', '2023-11-12', 'India'),
(16, 'Christmas', '2023-12-25', 'India'),
(17, 'New year', '2024-01-01', 'India');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authentication`
--
ALTER TABLE `authentication`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fest_india`
--
ALTER TABLE `fest_india`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authentication`
--
ALTER TABLE `authentication`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `fest_india`
--
ALTER TABLE `fest_india`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
