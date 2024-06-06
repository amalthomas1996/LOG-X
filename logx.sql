-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 08, 2024 at 05:16 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `logx`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_activity`
--

DROP TABLE IF EXISTS `admin_activity`;
CREATE TABLE IF NOT EXISTS `admin_activity` (
  `activityid` int NOT NULL AUTO_INCREMENT,
  `activityname` varchar(50) NOT NULL,
  PRIMARY KEY (`activityid`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin_activity`
--

INSERT INTO `admin_activity` (`activityid`, `activityname`) VALUES
(1, 'Planning'),
(2, 'Analysis'),
(3, 'Design'),
(4, 'Implimentation'),
(5, 'Testing'),
(6, 'Integration'),
(7, 'deployment'),
(8, 'Documentation'),
(9, 'Manitanance');

-- --------------------------------------------------------

--
-- Table structure for table `admin_employee`
--

DROP TABLE IF EXISTS `admin_employee`;
CREATE TABLE IF NOT EXISTS `admin_employee` (
  `empid` int NOT NULL AUTO_INCREMENT,
  `empname` varchar(20) NOT NULL,
  `empcode` varchar(20) NOT NULL,
  `role` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `teamid_id` int DEFAULT NULL,
  `projectid_id` int DEFAULT NULL,
  `assigndate` date NOT NULL,
  PRIMARY KEY (`empid`),
  KEY `Admin_employee_team_id_id_483ff718` (`teamid_id`),
  KEY `Admin_employee_projectid_id_7210b4ed` (`projectid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin_employee`
--

INSERT INTO `admin_employee` (`empid`, `empname`, `empcode`, `role`, `email`, `phone`, `photo`, `teamid_id`, `projectid_id`, `assigndate`) VALUES
(29, 'Amala Shibu', '78541', 'Project Manager', 'amalashibu2382001@gmail.com', '8075563190', 'download_1_HDmInA3.jpeg', 9, 12, '2024-04-11'),
(20, 'AMAL THOMAS', 'Admin', 'Admin', 'Admin', 'Admin', 'color_two.jpg', 9, NULL, '2024-04-11'),
(28, 'Amal Shajan', '856233', 'Employee', 'amalshajan345@gmail.com', '123456789', 'WhatsApp_Image30c.jpg', 9, 10, '2024-04-11'),
(27, 'Karthik Suresh', '856214', 'Employee', 'krtksrsh369@gmail.com', '9061701991', 'Spiderman.jpg', 9, NULL, '2024-04-11'),
(30, 'ammu', '4562', 'Project Manager', 'ammu@gmail.com', '123', '001_A24Zuha.jpg', 10, 11, '2024-04-11'),
(31, 'Jibin', '75689', 'Employee', 'jibin@gmail.com', '7895', 'WhatsApp_Image_2022-11-14_at_19.41.49.jpg', 9, 10, '2024-04-12'),
(33, 'Dona', '85621', 'Employee', 'dona@gmail.com', '123', 'STScI-01G79R51118N21AAZ9MZ8XWWQ6.png', 10, 11, '2024-04-12'),
(34, 'Jeevan', 'RY8116', 'Employee', 'jeevangeorgemyladoor003@gmail.com', '9188453066', 'images_2egamWb.jpeg', NULL, NULL, '2024-04-17'),
(35, 'JissyMol', 'AE7774', 'Employee', 'jissymoljiji99@gmail.com', '9074781566', 'images_1.jpeg', NULL, NULL, '2024-04-17'),
(36, 'sigma', 'BP3486', 'Employee', 'amalthomas106@gmail.com', '7845238475', 'pexels-iriser-1366957.jpg', NULL, NULL, '2024-05-07');

-- --------------------------------------------------------

--
-- Table structure for table `admin_login`
--

DROP TABLE IF EXISTS `admin_login`;
CREATE TABLE IF NOT EXISTS `admin_login` (
  `loginid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL,
  `empid_id` int NOT NULL,
  PRIMARY KEY (`loginid`),
  KEY `Admin_login_empid_id_4617c171` (`empid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin_login`
--

INSERT INTO `admin_login` (`loginid`, `username`, `password`, `role`, `empid_id`) VALUES
(27, 'jibin@gmail.com', '7895', 'Employee', 31),
(28, 'dona@gmail.com', '123', 'Employee', 33),
(25, 'amala', '0990', 'Project Manager', 29),
(26, 'ammu@gmail.com', '123', 'Project Manager', 30),
(16, 'Admin', 'Admin', 'Admin', 20),
(24, 'amalshajan', '0990', 'Employee', 28),
(23, 'krtksrsh369@gmail.com', '9061701990', 'Employee', 27),
(29, 'jeevangeorgemyladoor003@gmail.com', '9188453066', 'Employee', 34),
(30, 'krtksrsh369@gmail.com', '9061701991', 'Employee', 35),
(31, 'amalthomas106@gmail.com', '7845238475', 'Employee', 36);

-- --------------------------------------------------------

--
-- Table structure for table `admin_project`
--

DROP TABLE IF EXISTS `admin_project`;
CREATE TABLE IF NOT EXISTS `admin_project` (
  `projectid` int NOT NULL AUTO_INCREMENT,
  `projectname` varchar(20) NOT NULL,
  `projectdesc` varchar(100) NOT NULL,
  `projectdate` date NOT NULL,
  `projectcost` bigint NOT NULL,
  `startingdate` date NOT NULL,
  `enddate` date NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`projectid`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin_project`
--

INSERT INTO `admin_project` (`projectid`, `projectname`, `projectdesc`, `projectdate`, `projectcost`, `startingdate`, `enddate`, `status`) VALUES
(10, 'TeleX', 'Telecommunication Web App', '2024-04-01', 8000000, '2024-04-02', '2024-05-31', 'Pending'),
(9, 'Santhigiri', 'Santhigiri College Web Site', '2024-03-25', 7900000, '2024-05-01', '2024-05-31', 'Completed'),
(8, 'Shopsy ', 'Shopsy Shopping Web App', '2024-03-25', 100000, '2024-03-26', '2024-05-31', 'Pending'),
(11, 'Santhisoft', 'Santhisoft Web Site', '2024-04-12', 820000, '2024-04-13', '2024-05-30', 'Pending'),
(12, 'new', 'new', '2024-05-07', 800000, '2024-05-08', '2024-05-31', 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `admin_team`
--

DROP TABLE IF EXISTS `admin_team`;
CREATE TABLE IF NOT EXISTS `admin_team` (
  `teamid` int NOT NULL AUTO_INCREMENT,
  `description` varchar(50) NOT NULL,
  `projectid_id` int NOT NULL,
  `teamname` varchar(20) NOT NULL,
  PRIMARY KEY (`teamid`),
  KEY `Admin_team_project_id_id_a632fb43` (`projectid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin_team`
--

INSERT INTO `admin_team` (`teamid`, `description`, `projectid_id`, `teamname`) VALUES
(10, 'Team B', 9, 'B team'),
(9, 'team A', 8, 'A team');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add login', 7, 'add_login'),
(26, 'Can change login', 7, 'change_login'),
(27, 'Can delete login', 7, 'delete_login'),
(28, 'Can view login', 7, 'view_login'),
(29, 'Can add activity', 8, 'add_activity'),
(30, 'Can change activity', 8, 'change_activity'),
(31, 'Can delete activity', 8, 'delete_activity'),
(32, 'Can view activity', 8, 'view_activity'),
(33, 'Can add project', 9, 'add_project'),
(34, 'Can change project', 9, 'change_project'),
(35, 'Can delete project', 9, 'delete_project'),
(36, 'Can view project', 9, 'view_project'),
(37, 'Can add employee', 10, 'add_employee'),
(38, 'Can change employee', 10, 'change_employee'),
(39, 'Can delete employee', 10, 'delete_employee'),
(40, 'Can view employee', 10, 'view_employee'),
(41, 'Can add team', 11, 'add_team'),
(42, 'Can change team', 11, 'change_team'),
(43, 'Can delete team', 11, 'delete_team'),
(44, 'Can view team', 11, 'view_team'),
(45, 'Can add project task', 12, 'add_projecttask'),
(46, 'Can change project task', 12, 'change_projecttask'),
(47, 'Can delete project task', 12, 'delete_projecttask'),
(48, 'Can view project task', 12, 'view_projecttask'),
(49, 'Can add empassign', 13, 'add_empassign'),
(50, 'Can change empassign', 13, 'change_empassign'),
(51, 'Can delete empassign', 13, 'delete_empassign'),
(52, 'Can view empassign', 13, 'view_empassign'),
(53, 'Can add projectassigndata', 14, 'add_projectassigndata'),
(54, 'Can change projectassigndata', 14, 'change_projectassigndata'),
(55, 'Can delete projectassigndata', 14, 'delete_projectassigndata'),
(56, 'Can view projectassigndata', 14, 'view_projectassigndata');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'Admin', 'login'),
(8, 'Admin', 'activity'),
(9, 'Admin', 'project'),
(10, 'Admin', 'employee'),
(11, 'Admin', 'team'),
(12, 'ProjectManager', 'projecttask'),
(13, 'ProjectManager', 'empassign'),
(14, 'ProjectManager', 'projectassigndata');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-18 14:50:28.594493'),
(2, 'auth', '0001_initial', '2024-02-18 14:50:29.136191'),
(3, 'admin', '0001_initial', '2024-02-18 14:50:29.295611'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-18 14:50:29.301883'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-18 14:50:29.308985'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-18 14:50:29.371252'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-18 14:50:29.404462'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-18 14:50:29.444667'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-18 14:50:29.450781'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-18 14:50:29.492641'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-18 14:50:29.494693'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-18 14:50:29.502908'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-18 14:50:29.553469'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-18 14:50:29.586568'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-18 14:50:29.620676'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-18 14:50:29.626873'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-18 14:50:29.660263'),
(18, 'sessions', '0001_initial', '2024-02-18 14:50:29.697536'),
(19, 'Admin', '0001_initial', '2024-02-18 14:50:46.846356'),
(20, 'Admin', '0002_activity', '2024-02-19 15:26:58.073993'),
(21, 'Admin', '0003_project', '2024-02-21 05:04:48.427272'),
(22, 'Admin', '0004_employee_delete_login', '2024-02-21 13:42:52.489471'),
(23, 'Admin', '0005_login', '2024-02-21 13:43:13.272298'),
(24, 'Admin', '0006_delete_login', '2024-02-21 13:50:45.260133'),
(25, 'Admin', '0007_login', '2024-02-21 13:51:01.362782'),
(26, 'Admin', '0008_remove_login_empid_delete_employee_delete_login', '2024-02-21 14:08:28.628091'),
(27, 'Admin', '0009_employee_login', '2024-02-21 14:08:46.285340'),
(28, 'Admin', '0010_alter_project_enddate_alter_project_startingdate', '2024-02-22 10:41:59.350572'),
(29, 'Admin', '0011_alter_project_enddate_alter_project_startingdate', '2024-02-22 10:42:40.985143'),
(30, 'Admin', '0012_employee_status', '2024-02-26 04:48:13.473920'),
(31, 'Admin', '0013_team', '2024-02-26 05:41:31.910237'),
(32, 'Admin', '0014_employee_team_id', '2024-02-26 05:42:26.324718'),
(33, 'Admin', '0015_alter_employee_team_id', '2024-02-26 05:43:19.101842'),
(34, 'Admin', '0016_team_teamname', '2024-02-26 05:49:04.236830'),
(35, 'Admin', '0017_rename_team_id_employee_teamid', '2024-02-26 06:20:39.246345'),
(36, 'Admin', '0018_rename_project_id_team_projectid', '2024-02-26 08:55:34.659370'),
(37, 'ProjectManager', '0001_initial', '2024-02-26 14:24:09.393309'),
(38, 'ProjectManager', '0002_empassign', '2024-02-27 14:24:25.412468'),
(39, 'ProjectManager', '0003_empassign_projectid', '2024-02-28 10:31:05.186201'),
(40, 'Admin', '0019_alter_employee_status', '2024-03-25 15:02:40.107062'),
(41, 'Admin', '0020_remove_employee_status_employee_projectid', '2024-03-26 04:32:46.710359'),
(42, 'ProjectManager', '0004_empassign_rstatus', '2024-04-08 04:39:30.653134'),
(43, 'ProjectManager', '0005_remove_projecttask_status', '2024-04-09 06:47:07.093032'),
(44, 'Admin', '0021_employee_assigndate', '2024-04-11 07:19:42.651746'),
(45, 'ProjectManager', '0006_projectassigndata', '2024-04-11 08:47:12.505197'),
(46, 'Admin', '0022_project_status', '2024-04-11 09:03:07.348125'),
(47, 'ProjectManager', '0007_projectassigndata_status', '2024-04-11 09:04:31.456893'),
(48, 'Admin', '0023_alter_employee_projectid', '2024-04-11 10:01:47.665880'),
(49, 'Admin', '0024_alter_employee_teamid', '2024-04-12 04:23:56.231077');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('liu4ozan6ufc7duoe71jdr6wvjzjjuo3', 'eyJ1c2VybmFtZSI6ImFtYWxhc2hpYnUyMzgyMDAxQGdtYWlsLmNvbSIsImxvZ2luaWQiOjI1fQ:1rozIR:kyZnhuTM8Hruw272oLs5j6rEBI-FQbJ8wNEkA-Dlhr8', '2024-04-09 05:24:27.755894'),
('ehhitw06ch52yjhegztm4cv83vko7tt7', 'eyJ1c2VybmFtZSI6IkFkbWluIiwibG9naW5pZCI6MTZ9:1rvDyL:F57CHl-pFEZI6kVpkkFhWsQrNFIpOI1bFBbwrRnX9Qs', '2024-04-26 10:17:29.545148'),
('qh0g5gyul3v9z1undk3azzkikg5t43pc', 'eyJ1c2VybmFtZSI6ImFzIiwibG9naW5pZCI6MjR9:1ru5k3:YHC_hPzhgFoISePaDA8AfYh_YzkNJKJzvce3yHZTQ8c', '2024-04-23 07:18:03.531926'),
('jin2nranis2eguw8875u504yq8zjdsw2', 'eyJ1c2VybmFtZSI6IkFkbWluIiwibG9naW5pZCI6MTZ9:1rxhqh:hsKtPPlgJREbBuDt9vUYSwC5X4z8msF5HWoRvR9jiXU', '2024-05-03 06:35:51.222834'),
('c1jnwsmkdu90ef4yytk7ydmyj8w6bpin', 'eyJ1c2VybmFtZSI6ImFtYWxhIiwibG9naW5pZCI6MjV9:1s4M7e:N2eFVOs2gbpZhraehB4z9MbNDmWr4ZThk2tty35kMrg', '2024-05-21 14:48:50.915009');

-- --------------------------------------------------------

--
-- Table structure for table `projectmanager_empassign`
--

DROP TABLE IF EXISTS `projectmanager_empassign`;
CREATE TABLE IF NOT EXISTS `projectmanager_empassign` (
  `empassignid` int NOT NULL AUTO_INCREMENT,
  `assigndate` date NOT NULL,
  `duedate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `empid_id` int NOT NULL,
  `projecttaskid_id` int NOT NULL,
  `projectid_id` int NOT NULL,
  `rstatus` varchar(50) NOT NULL,
  PRIMARY KEY (`empassignid`),
  KEY `ProjectManager_empassign_empid_id_c676671a` (`empid_id`),
  KEY `ProjectManager_empassign_projecttaskid_id_5b44e280` (`projecttaskid_id`),
  KEY `ProjectManager_empassign_projectid_id_68ce8c03` (`projectid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `projectmanager_empassign`
--

INSERT INTO `projectmanager_empassign` (`empassignid`, `assigndate`, `duedate`, `status`, `empid_id`, `projecttaskid_id`, `projectid_id`, `rstatus`) VALUES
(16, '2024-03-26', '2024-04-01', 'Completed', 28, 13, 9, 'Confirmed'),
(15, '2024-03-26', '2024-04-28', 'Completed', 28, 13, 9, 'Confirmed'),
(14, '2024-03-25', '2024-05-30', '10-20 %', 27, 12, 8, 'Confirmed'),
(18, '2024-04-12', '2024-04-28', 'none', 31, 13, 10, 'none'),
(21, '2024-04-12', '2024-05-17', '10-20 %', 33, 13, 11, 'Confirmed'),
(22, '2024-04-19', '2024-05-22', '0-10 %', 28, 12, 10, 'Requested');

-- --------------------------------------------------------

--
-- Table structure for table `projectmanager_projectassigndata`
--

DROP TABLE IF EXISTS `projectmanager_projectassigndata`;
CREATE TABLE IF NOT EXISTS `projectmanager_projectassigndata` (
  `assignid` int NOT NULL AUTO_INCREMENT,
  `empid_id` int NOT NULL,
  `projectid_id` int NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`assignid`),
  KEY `ProjectManager_projectassigndata_empid_id_af22c29e` (`empid_id`),
  KEY `ProjectManager_projectassigndata_projectid_id_fb0a461d` (`projectid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `projectmanager_projectassigndata`
--

INSERT INTO `projectmanager_projectassigndata` (`assignid`, `empid_id`, `projectid_id`, `status`) VALUES
(3, 29, 9, 'Completed'),
(4, 30, 8, 'Pending'),
(5, 29, 10, 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `projectmanager_projecttask`
--

DROP TABLE IF EXISTS `projectmanager_projecttask`;
CREATE TABLE IF NOT EXISTS `projectmanager_projecttask` (
  `projecttaskid` int NOT NULL AUTO_INCREMENT,
  `description` varchar(50) NOT NULL,
  `startingdate` date NOT NULL,
  `enddate` date NOT NULL,
  `activityid_id` int NOT NULL,
  `projectid_id` int NOT NULL,
  PRIMARY KEY (`projecttaskid`),
  KEY `ProjectManager_projecttask_activityid_id_fcc6f28b` (`activityid_id`),
  KEY `ProjectManager_projecttask_projectid_id_658cf657` (`projectid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `projectmanager_projecttask`
--

INSERT INTO `projectmanager_projecttask` (`projecttaskid`, `description`, `startingdate`, `enddate`, `activityid_id`, `projectid_id`) VALUES
(13, 'deploy', '2024-04-11', '2024-04-19', 1, 8),
(12, 'design new landing page', '2024-04-12', '2024-05-31', 3, 9),
(16, 'gQa2micP4U', '2024-05-08', '2024-05-30', 3, 12),
(17, 'gQa2micP4U', '2024-05-08', '2024-05-31', 2, 12),
(18, 'gQa2micP4U', '2024-05-15', '2024-05-31', 8, 12);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
