#practica4.base de datos para el tecnologico
#autor:Gabriela Berenice Gomez Santiz
#\. C:\administraBASE\Practica6_C22270660.sql

CREATE DATABASE IF NOT EXISTS db_taller ;
CREATE DATABASE db_taller;
USE db_taller;

CREATE TABLE LineaIn (clave INT PRIMARY KEY,nombre VARCHAR(100));

CREATE TABLE Profesor (clave INT PRIMARY KEY,nombre VARCHAR(100));

CREATE TABLE Revisor (clave INT PRIMARY KEY,nombre VARCHAR(100));

CREATE TABLE Proyecto (clave INT PRIMARY KEY,nombre VARCHAR(100) ,clave_linea INT ,
FOREIGN KEY (clave_linea) REFERENCES LineaIn(clave));


CREATE TABLE Alumno (ncontrol VARCHAR(10) PRIMARY KEY,nombre VARCHAR(90) ,clave_proyecto INT ,
FOREIGN KEY (clave_proyecto) REFERENCES Proyecto(clave));

CREATE TABLE Asesoria (clave_proyecto INT,profesor INT,
PRIMARY KEY (clave_proyecto, profesor),
FOREIGN KEY (clave_proyecto) REFERENCES Proyecto(clave),
FOREIGN KEY (profesor) REFERENCES Profesor(clave));

CREATE TABLE Evaluacion (clave_proyecto INT,clave_revisor INT,calificacion DECIMAL(10,2),
PRIMARY KEY (clave_proyecto, clave_revisor),
FOREIGN KEY (clave_proyecto) REFERENCES Proyecto(clave),
FOREIGN KEY (clave_revisor) REFERENCES Revisor(clave));

CREATE TABLE Sala (clave INT PRIMARY KEY ,nombre VARCHAR(50),ncontrol VARCHAR(15),
FOREIGN KEY (ncontrol) REFERENCES Alumno(ncontrol));

CREATE TABLE Sesion (clave INT PRIMARY KEY ,clave_proyecto INT,hora TIME,
FOREIGN KEY (clave_proyecto) REFERENCES Proyecto(clave),
FOREIGN KEY (clave_sala) REFERENCES Sala(clave));

CREATE TABLE IF NOT EXISTS Usuario (id INT PRIMARY KEY,nombre VARCHAR(100),rol ENUM('Administrador', 'Profesor', 'Revisor', 'Alumno'),clave_profesor INT ,
clave_revisor INT ,clave_alumno VARCHAR(10),  
FOREIGN KEY (clave_profesor) REFERENCES Profesor(clave),
FOREIGN KEY (clave_revisor) REFERENCES Revisor(clave),
FOREIGN KEY (clave_alumno) REFERENCES Alumno(ncontrol));

CREATE TABLE evaluacion (id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,id_proyecto INT,id_indicador INT,calificacion DECIMAL(5,2),
FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto),
FOREIGN KEY (id_indicador) REFERENCES indicador(id_indicador));


CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON db_taller.* TO 'admin'@'localhost';

CREATE USER 'profesor'@'localhost' IDENTIFIED BY 'profesor123';
GRANT SELECT ON db_taller.Proyecto TO 'profesor'@'localhost';
GRANT SELECT, INSERT ON db_taller.Asesoria TO 'profesor'@'localhost';

CREATE USER 'alumno'@'localhost' IDENTIFIED BY 'alumno123';
GRANT SELECT ON db_taller.Proyecto TO 'alumno'@'localhost';
GRANT SELECT ON db_taller.Alumno TO 'alumno'@'localhost';

CREATE USER 'revisor'@'localhost' IDENTIFIED BY 'revisor123';
GRANT SELECT ON db_taller.Proyecto TO 'revisor'@'localhost';
GRANT SELECT, INSERT, UPDATE ON db_taller.Evaluacion TO 'revisor'@'localhost';

LOAD DATA INFILE '/C:\administraBASE/practica6_C22270660.csv'
INTO TABLE area_conocimiento
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
