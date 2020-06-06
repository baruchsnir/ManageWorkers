-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: manageworkers
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `workers_worker`
--

DROP TABLE IF EXISTS `workers_worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workers_worker` (
  `id` int NOT NULL AUTO_INCREMENT,
  `emploee_id` int NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone_number` varchar(12) NOT NULL,
  `hire_date` varchar(50) NOT NULL,
  `salary` int NOT NULL,
  `commission_pct` double NOT NULL,
  `manager_id` int NOT NULL,
  `picture` varchar(100) NOT NULL,
  `department_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `workers_worker_department_id_id_a150c961_fk_workers_d` (`department_id_id`),
  CONSTRAINT `workers_worker_department_id_id_a150c961_fk_workers_d` FOREIGN KEY (`department_id_id`) REFERENCES `workers_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workers_worker`
--

LOCK TABLES `workers_worker` WRITE;
/*!40000 ALTER TABLE `workers_worker` DISABLE KEYS */;
INSERT INTO `workers_worker` VALUES (119,100,'baruch','snir','baruchsnir@outlook.com','507221859','2009-04-20 00:00:00',24000,0.3,0,'baruch.jpg',4),(120,101,'James','Butt','jbutt@gmail.com','504845142','2010-04-01 00:00:00',34000,0.3,100,'James_Butt.jfif',5),(121,102,'Josephine','Darakjy','josephine_darakjy@darakjy.org','523749840','2009-10-05 00:00:00',34000,0.3,100,'Josephine_Darakjy.jfif',6),(122,103,'Mark','Zuckerberg','markz@venere.org','502644130','2009-01-07 00:00:00',33000,0.3,100,'Mark_Zuckerberg.jfif',7),(123,104,'Donette','Foller','donette.foller@cox.net','545701893','2009-10-09 00:00:00',30000,0.1,101,'Donette_Foller.jfif',5),(124,105,'Simona','Morasca','simona@morasca.com','548006759','2011-01-03 00:00:00',30000,0.1,101,'Simona_Morasca.jfif',5),(125,106,'Mitsue','Tollner','mitsue_tollner@yahoo.com','515736914','2011-01-03 00:00:00',29000,0.1,101,'Mitsue_Tollner.jfif',5),(126,107,'Leota','Dilliard','leota@hotmail.com','508131105','2012-01-06 00:00:00',20000,0.2,102,'Leota_Dilliard.jfif',6),(127,108,'Sage','Wieser','sage_wieser@cox.net','584142147','2013-01-01 00:00:00',20000,0.2,102,'Sage_Wieser.jfif',6),(128,109,'Kris','Marrier','kris@gmail.com','528044694','2013-01-07 00:00:00',20000,0.2,102,'Kris_Marrier.jfif',6),(129,111,'Abel','Maclead','amaclead@gmail.com','536773675','2013-01-01 00:00:00',21000,0.2,103,'Abel_Maclead.jtif',7),(130,112,'Kiley','Caldarera','kiley.caldarera@aol.com','502543084','2013-01-08 00:00:00',21000,0.2,103,'Kiley_Caldarera.jfif',7),(131,113,'Graciela','Ruta','gruta@cox.net','517808425','2013-01-09 00:00:00',27000,0.1,101,'Graciela_Ruta.jfif',5),(132,114,'Cammy','Albares','calbares@gmail.com','548417216','2013-09-09 00:00:00',27000,0.1,101,'Cammy_Albares.jfif',5),(133,115,'Mattie','Poquette','mattie@aol.com','529536360','2014-09-01 00:00:00',21000,0.2,102,'team_2.jpg',6),(134,116,'Daniel','Square','daniels@hotmail.com','542357959','2012-01-01 00:00:00',22000,0.2,102,'daniel_square.jfif',6),(135,117,'Gladys','rim','gladys.rim@rim.org','546619598','2013-11-01 00:00:00',20000,0.1,104,'team_3.jpg',5),(136,118,'Yuki','Whobrey','yuki_whobrey@aol.com','543414470','2013-10-01 00:00:00',20000,0.1,104,'team_4.jpg',5),(137,119,'Fletcher','Flosi','flosi@yahoo.com','524265657','2013-01-05 00:00:00',19000,0.2,110,'Fletcher_Flosi.jfif',7),(138,120,'Bette','Nicka','bette_nicka@cox.net','504924643','2013-05-05 00:00:00',19000,0.2,110,'Bette_Nicka.jfif',7),(139,110,'Minna','Amigon','minna_amigon@yahoo.com','554228694','2014-01-01 00:00:00',21000,0.2,103,'Minna_Amigon.jfif',7),(140,121,'Dave','Amigon','Dave_amigon@yahoo.com','554233694','01/11/2011',28000,0.2,100,'Dave_Amigon.jfif',8),(141,121,'Moses','Chohen','moses.choen@rim.org','546634531','11/03/2013',20000,0.1,121,'Moses_Chohen.jpg',8);
/*!40000 ALTER TABLE `workers_worker` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-20 19:35:54
