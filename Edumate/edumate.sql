-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 07, 2020 at 08:45 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edumate`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE `student_details` (
  `id` int(11) NOT NULL,
  `fullname` text NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL,
  `gender` text NOT NULL,
  `university` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`id`, `fullname`, `email`, `password`, `gender`, `university`) VALUES
(1, 'John Doe', 'john@gmail.com', '1234', 'male', 'Mumbai University'),
(2, 'aditya', 'rockstar@gmail.com', 'adi', 'male', 'Mumbai University');

-- --------------------------------------------------------

--
-- Table structure for table `student_records`
--

CREATE TABLE `student_records` (
  `id` int(11) NOT NULL,
  `subject_name` text NOT NULL,
  `marks_scored` int(3) NOT NULL,
  `out_off` int(3) NOT NULL,
  `credit_point` int(1) NOT NULL,
  `semester` int(1) NOT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_records`
--

INSERT INTO `student_records` (`id`, `subject_name`, `marks_scored`, `out_off`, `credit_point`, `semester`, `student_id`) VALUES
(8, 'IP', 95, 100, 5, 5, 1),
(9, 'IMP', 92, 100, 5, 5, 1),
(10, 'CNS', 88, 100, 5, 5, 1),
(11, 'ADMT', 85, 100, 5, 5, 1),
(12, 'MES', 81, 100, 5, 5, 1),
(13, 'BCE', 48, 50, 2, 5, 1),
(14, 'gdfsfv', 76, 100, 7, 1, 1),
(15, 'njn', 78, 100, 8, 1, 1),
(16, 'kjjkkoko', 98, 100, 9, 1, 1),
(17, 'okokok', 28, 100, 2, 1, 1),
(18, 'kok', 87, 100, 8, 1, 1),
(19, 'gtf', 99, 100, 9, 1, 1),
(20, 'math', 87, 100, 8, 3, 2),
(21, 'DLDA', 23, 100, 2, 3, 2),
(22, 'ECCF', 75, 100, 8, 3, 2),
(23, 'DM', 76, 100, 8, 3, 2),
(24, 'JAVA', 87, 100, 9, 3, 2),
(25, 'DS', 28, 100, 2, 3, 2),
(26, 'njhnj', 19, 100, 1, 2, 2),
(27, 'nnmk', 28, 100, 2, 2, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student_details`
--
ALTER TABLE `student_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_records`
--
ALTER TABLE `student_records`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student_details`
--
ALTER TABLE `student_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `student_records`
--
ALTER TABLE `student_records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
