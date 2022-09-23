-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema biblioteca
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema biblioteca
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `biblioteca` DEFAULT CHARACTER SET utf8 ;
USE `biblioteca` ;

-- -----------------------------------------------------
-- Table `biblioteca`.`generos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`generos` (
  `idgeneros` INT NOT NULL AUTO_INCREMENT,
  `genero` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idgeneros`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`autores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`autores` (
  `idautores` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idautores`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`editoras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`editoras` (
  `ideditoras` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`ideditoras`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`livros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`livros` (
  `idlivros` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NOT NULL,
  `id_genero` INT NOT NULL,
  `id_autor` INT NOT NULL,
  `paginas` INT NOT NULL,
  `terminado` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idlivros`),
  INDEX `fk_livros_1_idx` (`id_genero` ASC) VISIBLE,
  INDEX `fk_livros_2_idx` (`id_autor` ASC) VISIBLE,
  CONSTRAINT `fk_livros_1`
    FOREIGN KEY (`id_genero`)
    REFERENCES `biblioteca`.`generos` (`idgeneros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livros_2`
    FOREIGN KEY (`id_autor`)
    REFERENCES `biblioteca`.`autores` (`idautores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`livros_editoras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`livros_editoras` (
  `idlivros_editoras` INT NOT NULL AUTO_INCREMENT,
  `id_livro` INT NOT NULL,
  `id_editora` INT NOT NULL,
  PRIMARY KEY (`idlivros_editoras`),
  INDEX `fk_livros_editoras_1_idx` (`id_livro` ASC) VISIBLE,
  INDEX `fk_livros_editoras_2_idx` (`id_editora` ASC) VISIBLE,
  CONSTRAINT `fk_livros_editoras_1`
    FOREIGN KEY (`id_livro`)
    REFERENCES `biblioteca`.`livros` (`idlivros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livros_editoras_2`
    FOREIGN KEY (`id_editora`)
    REFERENCES `biblioteca`.`editoras` (`ideditoras`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`complementos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`complementos` (
  `idcomplementos` INT NOT NULL AUTO_INCREMENT,
  `id_livro_base` INT NOT NULL,
  `id_livro_complementar` INT NOT NULL,
  PRIMARY KEY (`idcomplementos`),
  INDEX `fk_complementos_1_idx` (`id_livro_base` ASC) VISIBLE,
  INDEX `fk_complementos_2_idx` (`id_livro_complementar` ASC) VISIBLE,
  CONSTRAINT `fk_complementos_1`
    FOREIGN KEY (`id_livro_base`)
    REFERENCES `biblioteca`.`livros` (`idlivros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_complementos_2`
    FOREIGN KEY (`id_livro_complementar`)
    REFERENCES `biblioteca`.`livros` (`idlivros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
