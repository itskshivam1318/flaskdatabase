-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2020 at 03:30 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fatigue`
--

-- --------------------------------------------------------

--
-- Table structure for table `ques1`
--

CREATE TABLE `ques1` (
  `que1` int(11) NOT NULL,
  `que2` int(11) NOT NULL,
  `que3` int(11) NOT NULL,
  `que4` int(11) NOT NULL,
  `que5` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ques1`
--

INSERT INTO `ques1` (`que1`, `que2`, `que3`, `que4`, `que5`) VALUES
(2, 4, 3, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `ques2`
--

CREATE TABLE `ques2` (
  `que6` int(11) NOT NULL,
  `que7` int(11) NOT NULL,
  `que8` int(11) NOT NULL,
  `que9` int(11) NOT NULL,
  `que10` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ques2`
--

INSERT INTO `ques2` (`que6`, `que7`, `que8`, `que9`, `que10`) VALUES
(1, 4, 3, 3, 5);

-- --------------------------------------------------------

--
-- Table structure for table `ques3`
--

CREATE TABLE `ques3` (
  `que11` int(11) NOT NULL,
  `que12` int(11) NOT NULL,
  `que13` int(11) NOT NULL,
  `que14` int(11) NOT NULL,
  `que15` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ques3`
--

INSERT INTO `ques3` (`que11`, `que12`, `que13`, `que14`, `que15`) VALUES
(1, 5, 2, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `ques4`
--

CREATE TABLE `ques4` (
  `que16` int(11) NOT NULL,
  `que17` int(11) NOT NULL,
  `que18` int(11) NOT NULL,
  `que19` int(11) NOT NULL,
  `que20` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ques4`
--

INSERT INTO `ques4` (`que16`, `que17`, `que18`, `que19`, `que20`) VALUES
(3, 5, 1, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `fname` varchar(60) NOT NULL,
  `lname` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `fname`, `lname`, `email`, `gender`, `age`) VALUES
(1, 'shivam', 'kharje', 'shivamkharje123@gmail.com', 'male', 22),
(2, 'ramesh ', 'kale', 'rameshkale@gmail.com', 'male', 22),
(3, 'shravani', 'kamat', 'shravanikamat@gmail.com', 'female', 22),
(4, 'tamish', 'sawant', 'tamishsawant@gmail.com', 'male', 22),
(5, 'dhaval', 'shah', 'dhavalshah@gmail.com', 'male', 22);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
