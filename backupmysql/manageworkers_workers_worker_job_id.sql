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
-- Table structure for table `workers_worker_job_id`
--

DROP TABLE IF EXISTS `workers_worker_job_id`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workers_worker_job_id` (
  `id` int NOT NULL AUTO_INCREMENT,
  `worker_id` int NOT NULL,
  `job_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `workers_worker_job_id_worker_id_job_id_a9706a9f_uniq` (`worker_id`,`job_id`),
  KEY `workers_worker_job_id_job_id_03513bfc_fk_workers_job_id` (`job_id`),
  CONSTRAINT `workers_worker_job_id_job_id_03513bfc_fk_workers_job_id` FOREIGN KEY (`job_id`) REFERENCES `workers_job` (`id`),
  CONSTRAINT `workers_worker_job_id_worker_id_066f8fdc_fk_workers_worker_id` FOREIGN KEY (`worker_id`) REFERENCES `workers_worker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=180 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workers_worker_job_id`
--

LOCK TABLES `workers_worker_job_id` WRITE;
/*!40000 ALTER TABLE `workers_worker_job_id` DISABLE KEYS */;
INSERT INTO `workers_worker_job_id` VALUES (152,119,18),(153,120,19),(154,121,20),(155,122,21),(156,123,23),(157,123,24),(158,123,25),(159,124,23),(160,124,25),(161,125,23),(162,126,26),(163,127,26),(164,128,26),(165,129,27),(166,130,27),(167,131,23),(168,132,23),(169,133,26),(170,134,26),(171,135,23),(172,136,23),(173,137,27),(174,137,28),(175,138,27),(176,138,29),(177,139,27),(178,140,22),(179,141,31);
/*!40000 ALTER TABLE `workers_worker_job_id` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-20 19:35:55
