-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 03, 2026 at 10:34 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tsbd_website`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(25, 'Can add product', 7, 'add_product'),
(26, 'Can change product', 7, 'change_product'),
(27, 'Can delete product', 7, 'delete_product'),
(28, 'Can view product', 7, 'view_product'),
(29, 'Can add post', 8, 'add_post'),
(30, 'Can change post', 8, 'change_post'),
(31, 'Can delete post', 8, 'delete_post'),
(32, 'Can view post', 8, 'view_post'),
(33, 'Can add team member', 9, 'add_teammember'),
(34, 'Can change team member', 9, 'change_teammember'),
(35, 'Can delete team member', 9, 'delete_teammember'),
(36, 'Can view team member', 9, 'view_teammember');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blog_post`
--

CREATE TABLE `blog_post` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(8, 'blog', 'post'),
(5, 'contenttypes', 'contenttype'),
(7, 'products', 'product'),
(6, 'sessions', 'session'),
(9, 'team', 'teammember');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-08-11 18:27:30.590969'),
(2, 'auth', '0001_initial', '2026-08-11 18:27:38.638477'),
(3, 'admin', '0001_initial', '2026-08-11 18:27:41.125603'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-08-11 18:27:41.159253'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-08-11 18:27:41.216076'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-08-11 18:27:41.846077'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-08-11 18:27:42.845542'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-08-11 18:27:42.994142'),
(9, 'auth', '0004_alter_user_username_opts', '2026-08-11 18:27:43.027655'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-08-11 18:27:43.525534'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-08-11 18:27:43.579728'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-08-11 18:27:43.719742'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-08-11 18:27:43.816585'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-08-11 18:27:43.936932'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-08-11 18:27:44.094940'),
(16, 'auth', '0011_update_proxy_permissions', '2026-08-11 18:27:44.142929'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-08-11 18:27:44.345716'),
(18, 'sessions', '0001_initial', '2026-08-11 18:27:44.827850'),
(19, 'blog', '0001_initial', '2026-08-17 07:13:16.528427'),
(20, 'products', '0001_initial', '2026-08-17 07:13:16.708892'),
(21, 'products', '0002_delete_product', '2026-08-18 14:43:38.777941'),
(22, 'team', '0001_initial', '2026-08-19 15:40:10.195189'),
(23, 'team', '0002_initial', '2026-08-19 15:40:10.221789'),
(24, 'team', '0001_add_phone_and_slug', '2026-08-24 07:58:58.278487'),
(25, 'services', '0001_service_modules', '2026-08-29 17:31:01.295018'),
(26, 'products', '0003_product_modules', '2026-08-30 19:16:06.431333');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tsbd_blog`
--

CREATE TABLE `tsbd_blog` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `short_description` text DEFAULT NULL,
  `content` longtext DEFAULT NULL,
  `image` varchar(500) DEFAULT '',
  `author` varchar(150) DEFAULT '',
  `status` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tsbd_products`
--

CREATE TABLE `tsbd_products` (
  `id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_details` text DEFAULT NULL,
  `image` varchar(500) DEFAULT '',
  `status` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tsbd_products`
--

INSERT INTO `tsbd_products` (`id`, `product_name`, `product_details`, `image`, `status`) VALUES
(7, 'Diagnosis Management System', 'The Diagnosis Management System has been developed for helping diagnostic centers and hospitals manage their routine operations more effectively using a centralized software system. The software will be able to manage patients, doctors, scheduling, diagnosis tests, test results, billings, and health records. The software helps to decrease paperwork, organize patients\' data, optimize the workflow in laboratories, and ensure that reports are prepared promptly. Using a user-friendly interface and centralized data management system helps increase the efficiency of the operations.', 'products/images (1).jpg', 1),
(8, 'Pharmacy Management System', 'With our Pharmacy Management System, it becomes easy for pharmacies to manage their medicines, inventories, sales, purchases, vendors, clients, and other activities through one single software. This software can monitor the medicines’ inventory, batch number, expiry date, purchase details, sales details, and low stock notifications. Moreover, this software can keep the details of products up-to-date, produce invoices, and create reports too. Through this software, pharmacies can become more efficient and precise in managing their products.', 'products/pharmacy-management.jpg', 1),
(9, 'Prescription Management System', 'Through our Prescription Management System, health practitioners have been able to manage their prescription details in one convenient place. This system has been able to help the healthcare professionals in managing the details regarding the patient\'s data, doctors\' information, medication, dosage instruction, prescriptions history, and follow-ups. Our system is easy to use, and it ensures that all the prescription details have been streamlined in one place.', 'products/PreviewImage.jpg', 1),
(10, 'Inventory Management System', 'The Inventory Management System makes it easy for business owners to manage their products, stock, purchasing, selling, supplier information, and general inventory activities through one application. The Inventory Management System has the following features; it enables real-time stock tracking, product classification, low stock alerts, stock in and stock out management, as well as generates inventory reports. Through such capabilities, the system will help keep an efficient stock level within the business.', 'products/images.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tsbd_product_modules`
--

CREATE TABLE `tsbd_product_modules` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `module_number` int(11) NOT NULL,
  `title` varchar(255) NOT NULL DEFAULT '',
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tsbd_product_modules`
--

INSERT INTO `tsbd_product_modules` (`id`, `product_id`, `module_number`, `title`, `description`) VALUES
(1, 10, 1, 'Product & Stock Management', 'Maintain products, categories, units and stock information in one organized system.'),
(2, 10, 2, 'Purchase & Supplier Management', 'Track suppliers, purchase records and incoming stock to keep procurement organized.'),
(3, 10, 3, 'Sales & Stock Transactions', 'Manage sales transactions and automatically maintain accurate stock movement records.'),
(4, 10, 4, 'Reporting & Analytics', 'Generate useful reports for stock position, sales activity, purchases and business performance.'),
(5, 10, 5, 'User Access & System Control', 'Support role-based access, operational control and reliable management of day-to-day inventory activities.'),
(6, 9, 1, 'Patient Prescription Records', 'Organize prescription information and maintain accessible records for efficient clinical and pharmacy workflows.'),
(7, 9, 2, 'Prescription Entry & Processing', 'Record and process prescription details in a structured format to reduce manual errors and improve workflow efficiency.'),
(8, 9, 3, 'Medicine & Dosage Information', 'Manage medicine names, dosage instructions and related prescription information in a clear and consistent format.'),
(9, 9, 4, 'Prescription History & Tracking', 'Keep historical prescription records available for review, monitoring and operational reference.'),
(10, 9, 5, 'Reports & Management Insights', 'Provide structured reports and summaries to support better administrative visibility and decision-making.'),
(11, 8, 1, 'Medicine & Inventory Management', 'Manage medicine catalogs, stock levels, expiry information and inventory movement from a centralized system.'),
(12, 8, 2, 'Sales & Billing', 'Handle pharmacy sales and billing workflows with organized transaction records for day-to-day operations.'),
(13, 8, 3, 'Purchase & Supplier Management', 'Track medicine purchases, suppliers and receiving activities to maintain a reliable supply workflow.'),
(14, 8, 4, 'Expiry & Stock Monitoring', 'Monitor expiry dates and stock conditions to support timely action and reduce inventory-related risks.'),
(15, 8, 5, 'Reports & Business Analytics', 'Generate operational reports covering sales, purchases, inventory and other key pharmacy activities.'),
(16, 7, 1, 'Patient Information Management', 'Maintain structured patient information to support efficient diagnosis and service workflows.'),
(17, 7, 2, 'Diagnosis Record Management', 'Record diagnosis information in an organized format for easy access, review and operational continuity.'),
(18, 7, 3, 'Test & Result Tracking', 'Manage diagnostic test information and results with clear records for better information handling.'),
(19, 7, 4, 'History & Reporting', 'Keep diagnosis history and generate structured reports to support monitoring and administrative review.'),
(20, 7, 5, 'Secure Workflow Management', 'Provide controlled access and organized workflows to help maintain reliable and responsible information management.');

-- --------------------------------------------------------

--
-- Table structure for table `tsbd_projects`
--

CREATE TABLE `tsbd_projects` (
  `id` int(11) NOT NULL,
  `project_name` varchar(200) NOT NULL,
  `project_details` text DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `status` tinyint(1) DEFAULT 1,
  `image` varchar(255) DEFAULT NULL,
  `damo_link` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tsbd_projects`
--

INSERT INTO `tsbd_projects` (`id`, `project_name`, `project_details`, `service_id`, `status`, `image`, `damo_link`) VALUES
(1, 'Quantum Attendance & Healing Management System', 'An enterprise-grade administrative dashboard designed to manage client, track live attendance entries via QR/Registration lookup components and monitor corporate event participants effortlessly.', 2, 1, 'projects/quantum.logo.jpeg', 'https://quantumpy.teamsolutionsbangladesh.com'),
(6, 'Bank Bima Arthonity Core Platform', 'A comprehensive multi-tenant enterprise resource planning software featuring advanced modules for structural HR & payroll, customized pharmacy inventories, corporate transaction auditing, and custom permission settings.', 2, 1, 'projects/Screenshot (132).png', 'https://demo.teamsolutionsbangladesh.com/login'),
(7, 'Diet Counselling Center Patient Management', 'A specialized digital healthcare system built with a robust Patient Report Form Builder, custom metrics calculation tools (like BMI tracking), prescription storage databases, and integrated localized font engine toggles.', 3, 1, 'projects/Diet.logo.jpeg', 'https://dcc.teamsolutionsbangladesh.com'),
(8, 'TSBD Academy Learning Management Web Environment', 'A clean, modern project-first educational platform offering structured programming modules, live dashboard portals, and interactive search funnels to transform tech learners into job-ready developers.', 4, 1, 'projects/TSBD.jpeg', 'https://academy.teamsolutionsbangladesh.com');

-- --------------------------------------------------------

--
-- Table structure for table `tsbd_services`
--

CREATE TABLE `tsbd_services` (
  `id` int(11) NOT NULL,
  `service_name` varchar(200) NOT NULL,
  `service_details` text DEFAULT NULL,
  `status` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tsbd_services`
--

INSERT INTO `tsbd_services` (`id`, `service_name`, `service_details`, `status`) VALUES
(1, 'Software Solution', 'We offer reliable and tailored software solutions which are designed to meet the particular requirements of businesses and organisations. These solutions aid in the automation of daily operations, the streamlining of workflows, the efficient management of data, and the improvement of overall productivity. Whether it is business management systems or web applications or custom enterprise solutions, we create software that is scalable, easy to use and secure in order to help businesses work more intelligently and grow more quickly.', 1),
(2, 'Web Development', 'We develop websites that are up-to-date, interactive, and user-friendly to cater to all your business requirements. The web development services that we provide emphasize on a neat design, good performance, mobile-friendly nature, security, and ease of management. We can develop web applications, e-commerce websites, and other types of websites depending on your requirements.', 1),
(3, 'Software Development', 'We deliver software development services customized according to the unique requirements of businesses and other institutions. Whether it is business management software or enterprise applications, our software development involves building scalable, efficient, and secure applications. The software development process at our company revolves around business requirement analysis, workflow improvement, feature integration, and more.', 1),
(4, 'Training & Internship', 'Practical training and internships have been developed by us to ensure that students and professionals can gain practical technical skills. Practical learning, project work, industry knowledge, and professional skills are taught in our courses in various disciplines including software development, web development, testing, and many more IT technologies. Through our guided projects and tasks, learners can gain valuable experience as well as confidence to start their careers in the future.', 1),
(5, 'Affiliate Marketing', 'We offer affiliate marketing solutions that aid businesses and individuals in promoting any product or service via online marketing channels. Our solutions center on connecting brands with their relevant audience members, increasing brand visibility, and delivering results through affiliate marketing channels. We assist clients in planning campaigns, promoting affiliates, measuring performance, and compiling reports in order to increase business exposure and growth opportunities.', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tsbd_service_modules`
--

CREATE TABLE `tsbd_service_modules` (
  `id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `module_number` int(11) NOT NULL,
  `title` varchar(255) NOT NULL DEFAULT '',
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tsbd_service_modules`
--

INSERT INTO `tsbd_service_modules` (`id`, `service_id`, `module_number`, `title`, `description`) VALUES
(1, 1, 1, 'Requirement Analysis', 'We analyze your business requirements, workflow, challenges and goals to identify the right software solution.'),
(2, 1, 2, 'Solution Planning', 'We plan the system architecture, features, database structure and technologies required for the project.'),
(3, 1, 3, 'Development & Integration', 'We develop customized software and integrate databases, APIs and other required services.'),
(4, 1, 4, 'Testing & Deployment', 'We thoroughly test the system, resolve issues and deploy the completed solution.'),
(5, 1, 5, 'Support & Maintenance', 'We provide ongoing technical support, maintenance and future improvements.'),
(6, 2, 1, 'Requirement & Research', 'We understand your business goals, target audience and website requirements.'),
(7, 2, 2, 'UI/UX Design', 'We create a clean, responsive and user-friendly interface designed around your users.'),
(8, 2, 3, 'Frontend & Backend Development', 'We develop the complete website with modern frontend and reliable backend technologies.'),
(9, 2, 4, 'Testing & Optimization', 'We test functionality, responsiveness, performance and compatibility across devices.'),
(10, 2, 5, 'Deployment & Maintenance', 'We deploy your website and provide ongoing updates, maintenance and technical support.'),
(11, 3, 1, 'Business Analysis', 'We analyze your business processes and identify the software requirements.'),
(12, 3, 2, 'Architecture & Planning', 'We design a scalable architecture, database structure and technical roadmap.'),
(13, 3, 3, 'Custom Development', 'We build customized software according to your specific business requirements.'),
(14, 3, 4, 'QA & Security Testing', 'We test the software thoroughly to ensure reliability, usability, performance and security.'),
(15, 3, 5, 'Deployment & Support', 'We deploy the software and provide continuous technical support and improvements.'),
(16, 4, 1, 'Program Orientation', 'Participants are introduced to the program, learning objectives, tools and professional expectations.'),
(17, 4, 2, 'Learning & Fundamentals', 'Participants learn core concepts and practical technologies through structured training.'),
(18, 4, 3, 'Practical Projects', 'Participants work on hands-on projects to apply their technical knowledge in practical situations.'),
(19, 4, 4, 'Industry-Based Practice', 'Participants gain practical experience through real-world tasks and professional workflows.'),
(20, 4, 5, 'Evaluation & Certification', 'Performance is evaluated and successful participants receive appropriate completion recognition.'),
(21, 5, 1, 'Market & Audience Research', 'We research target audiences, market trends and relevant product opportunities.'),
(22, 5, 2, 'Offer & Product Selection', 'We identify suitable products and offers that align with the target audience.'),
(23, 5, 3, 'Content & Campaign Planning', 'We develop content and promotional strategies designed to reach potential customers.'),
(24, 5, 4, 'Promotion & Conversion', 'We promote selected offers through suitable digital channels and optimize conversion opportunities.'),
(25, 5, 5, 'Performance Tracking & Optimization', 'We monitor campaign performance and improve strategies based on measurable results.');

-- --------------------------------------------------------

--
-- Table structure for table `tsbd_team`
--

CREATE TABLE `tsbd_team` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `designation` varchar(150) DEFAULT '',
  `bio` text DEFAULT NULL,
  `image` varchar(500) DEFAULT '',
  `email` varchar(254) DEFAULT '',
  `linkedin` varchar(500) DEFAULT '',
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `phone` varchar(50) DEFAULT '',
  `slug` varchar(180) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tsbd_team`
--

INSERT INTO `tsbd_team` (`id`, `name`, `designation`, `bio`, `image`, `email`, `linkedin`, `status`, `phone`, `slug`) VALUES
(1, 'Simi Chakma', 'Junior Software Engineer', 'Computer Science and Engineering graduate with hands-on experience in software development. Currently working as an Intern at *Team Solutions Bangladesh*, where I am developing practical skills in Django, database management, frontend development, and software solutions. A motivated and dedicated learner who enjoys solving problems, exploring new technologies, and contributing to real-world projects.', 'team/WhatsApp Image 2026-08-24 at 13.27.19.jpeg', 'simi@gmail.com', 'https://www.linkedin.com/in/simi-chakma-518110227/', 1, '+880 1747-016786', 'simi'),
(4, 'Tahiyat Ahmed', 'Software Engineer', 'I am a Full-Stack Developer with a strong focus on backend engineering using Django and Laravel. Currently working as a Junior Software Developer, I build scalable web applications, ERP systems, and RESTful APIs that are designed for performance, reliability, and real-world usability.', 'team/1729169322097 (1).jpeg', 'tahiyat.ahmed703@gmail.com', 'https://www.linkedin.com/in/tahiyat-ahmed/', 1, '01858937589', 'tahiyat-ahmed'),
(5, 'Nafisa Anjum Moon', 'Software Engineer', 'Computer Science & Engineering graduate with a passion for web development and building user-friendly digital experiences. Currently working as a Software Engineer, constantly learning, solving problems, and exploring new technologies. Outside of work, I enjoy reading, creating content, and discovering little things that make life more cozy.', 'team/WhatsApp Image 2026-08-24 at 13.35.25.jpeg', 'nafisaanjummoon48@gmail.com', 'https://www.linkedin.com/in/nafisaanjummoon48/', 1, '01779451548', 'nafisa-moon'),
(6, 'Md. Tajuddin', 'Junior Software Engineer', 'I am a Full-Stack Developer specializing in Python, Django, PHP, and MySQL, with experience building scalable web applications and enterprise ERP systems. I focus on backend development, REST APIs, database management, automation, and responsive frontend solutions.\r\n\r\nI am also passionate about AI/ML, with experience as a published AI researcher and Mendeley contributor. I enjoy transforming complex business requirements into secure, scalable, and user-focused digital solutions.\r\n\r\nCore Expertise: Python • Django • PHP • MySQL • ERP • REST APIs • AI/ML • Database Design • Research & Innovation', 'team/WhatsApp Image 2026-08-24 at 13.24.10.jpeg', 'mdtajuddin0069@gmail.com', 'https://www.linkedin.com/in/md-tajuddin-08134022b/', 1, '+880 1754-713814', 'md-tajuddin');

-- --------------------------------------------------------

--
-- Table structure for table `website_contact_message`
--

CREATE TABLE `website_contact_message` (
  `id` bigint(20) NOT NULL,
  `name` varchar(120) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `subject` varchar(200) DEFAULT NULL,
  `message` longtext NOT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `website_contact_message`
--

INSERT INTO `website_contact_message` (`id`, `name`, `email`, `phone`, `subject`, `message`, `created_at`) VALUES
(1, 'Md. Tajuddin', 'ts.workspace26@gmail.com', '', '', 'hii', '2026-08-15 23:09:46'),
(2, 'Md. Tajuddin', 'ts.workspace26@gmail.com', '5121355', 'hi', 'kljklkl', '2026-08-15 23:10:08');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `blog_post`
--
ALTER TABLE `blog_post`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tsbd_blog`
--
ALTER TABLE `tsbd_blog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tsbd_products`
--
ALTER TABLE `tsbd_products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tsbd_product_modules`
--
ALTER TABLE `tsbd_product_modules`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_tsbd_product_module` (`product_id`,`module_number`),
  ADD KEY `idx_tsbd_product_modules_product` (`product_id`);

--
-- Indexes for table `tsbd_projects`
--
ALTER TABLE `tsbd_projects`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tsbd_services`
--
ALTER TABLE `tsbd_services`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tsbd_service_modules`
--
ALTER TABLE `tsbd_service_modules`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_tsbd_service_module` (`service_id`,`module_number`),
  ADD KEY `idx_tsbd_service_modules_service` (`service_id`);

--
-- Indexes for table `tsbd_team`
--
ALTER TABLE `tsbd_team`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tsbd_team_slug_unique` (`slug`),
  ADD KEY `idx_tsbd_team_status_order` (`status`,`id`);

--
-- Indexes for table `website_contact_message`
--
ALTER TABLE `website_contact_message`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blog_post`
--
ALTER TABLE `blog_post`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `tsbd_blog`
--
ALTER TABLE `tsbd_blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tsbd_products`
--
ALTER TABLE `tsbd_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tsbd_product_modules`
--
ALTER TABLE `tsbd_product_modules`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `tsbd_projects`
--
ALTER TABLE `tsbd_projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tsbd_services`
--
ALTER TABLE `tsbd_services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `tsbd_service_modules`
--
ALTER TABLE `tsbd_service_modules`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `tsbd_team`
--
ALTER TABLE `tsbd_team`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `website_contact_message`
--
ALTER TABLE `website_contact_message`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
