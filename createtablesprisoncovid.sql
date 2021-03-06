-- MySQL Script generated by MySQL Workbench
-- Sun Dec  6 23:17:56 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
-- SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE="";

-- -----------------------------------------------------
-- Schema prisoncovid
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema prisoncovid
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `prisoncovid` DEFAULT CHARACTER SET utf8 ;
USE `prisoncovid` ;

-- -----------------------------------------------------
-- Table `prisoncovid`.`state`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `prisoncovid`.`state` ;

CREATE TABLE IF NOT EXISTS `prisoncovid`.`state` (
  `state_date` DATE NOT NULL,
  `state_name` VARCHAR(100) NOT NULL,
  `state_cases` INT NOT NULL,
  `state_deaths` INT NOT NULL,
  PRIMARY KEY (`state_date`, `state_name`));



-- -----------------------------------------------------
-- Table `prisoncovid`.`county`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `prisoncovid`.`county` ;

CREATE TABLE IF NOT EXISTS `prisoncovid`.`county` (
  `county_date` DATE NOT NULL,
  `county_name` VARCHAR(100) NOT NULL,
  `state_name` VARCHAR(100) NOT NULL,
  `county_cases` INT NOT NULL,
  `county_deaths` INT NOT NULL,
  PRIMARY KEY (`county_date`, `county_name`, `state_name`));

-- -----------------------------------------------------
-- Table `prisoncovid`.`prison`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `prisoncovid`.`prison` ;

CREATE TABLE IF NOT EXISTS `prisoncovid`.`prison` (
  `prison_date` DATE NOT NULL,
  `prison_name` VARCHAR(100) NOT NULL,
  `state_name` VARCHAR(100) NOT NULL,
  `prison_cases` INT NOT NULL,
  `prison_dead` INT NOT NULL,
  PRIMARY KEY (`prison_date`, `prison_name`,`state_name`));
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
