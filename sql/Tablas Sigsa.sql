SELECT current_user;

----------------------------------------------------------------------------------------------------------

CREATE TABLE empleados(
num_nomina INTEGER PRIMARY KEY,
nombre VARCHAR(70),
email VARCHAR(70),
jefe_directo INTEGER,
departamento VARCHAR(70),
fecha_ingreso DATE,
is_active varchar(30),
sucursal varchar(50),
password varchar(100),
rol_user varchar(30)
)

ALTER TABLE empleados

SELECT*FROM empleados;

DROP TABLE empleados;
DELETE FROM empleados;

INSERT INTO empleados VALUES
(3009,'Carvajal Rodriguez Bryan','bcarvajal@sigsa.info','1504','Coordinador de Proyectos de Desarrollo','26-03-2018','true','Villahermosa,Tab','1234','normal'),

(1347,'Aguilar Potenciano Socorro','','1568','Cordinacion Administrativa','2014-06-06','true','Villahermosa,Tab','1234','normal'),
(1331,'Alcudia Leon Juan Manuel','jalcudia@sigsa.info','1322','Cordinacion de Proyectos SIG','2006-11-16','true','Villahermosa,Tab','1234','normal'),
(1308,'Baeza Chable Hugo','hbaeza@sigsa.info','1322','Cordinacion de Proyectos SIG','2010-02-22','true','Villahermosa,Tab','1234','normal'),
(1763,'Celorio Ulin Ninive Cristel','ninive.celorio@sigsa.info','1568','Cordinacion Administrativa','2012-07-03','true','Villahermosa,Tab','1234','normal'),
(1568,'Duran Andrade Diana Guadalupe','diana.duran@sigsa.info','1356','Produccion Cartografica','2011-04-13','true','Villahermosa,Tab','1234','administrador'),
(1313,'Gallardo Hernandez Maria de los Angeles','mgallardo@sigsa.info','1322','Cordinacion de Proyectos SIG','05-05-2003','true','Villahermosa,Tab','1234','normal'),
(1504,'Jimenez Prats Salvador','sjimenez@sigsa.info','1356','Produccion Cartografica','2010-02-23','true','Villahermosa,Tab','1234','administrador'),
(1598,'Lazaro Perez Kheila Idaly','idali.lazaro@sigsa.info','1504','Coordinador de Proyectos de Desarrollo','26-03-2018','true','Villahermosa,Tab','1234','normal'),
(1322,'Ricardez Mendez Hilario','hricardez@sigsa.info','1356','Produccion Cartografica','2006-02-03','true','Villahermosa,Tab','1234','normal'),
(1356,'Villegas Jeronimo Jose Gerardo','jvillegas@sigsa.info','1010','Produccion Cartografica','2007-10-29','true','Villahermosa,Tab','1234','administrador'),
(1628,'Duilio De Carmen Tosca','duilio.tosca@sigsa.info','1322','Cordinacion de Proyectos SIG','2018-11-16','true','Villahermosa,Tab','1234','normal'),
(501682,'Gonzalez Mendez Juan Bernardo','juan.gonzalez@sigsa.com.mx','1504','Coordinador de Proyectos de Desarrollo','2019-11-11','true','Villahermosa,Tab','1234','normal'),
(501684,'Gomez Rodriguez Dario','dario.gomez@sigsa.info','1322','Cordinacion de Proyectos SIG','2020-02-17','true','Villahermosa,Tab','1234','normal'),
(101474,'Lopez Olmedo Gustavo','gustavo.lopez@sigsa.info','1322','Cordinacion de Proyectos SIG','2009-02-16','true','Villahermosa,Tab','1234','normal'),
(501694,'Almeyda Canepa Hugo Isidoro','hugo.almeyda@sigsa.com.mx','1322','Cordinacion de Proyectos SIG','08-10-2020','true','Villahermosa,Tab','1234','normal'),
(501695,'Massieu Aladro Carlos Del Sagrado Corazon De Jesus','carlos.massieu@sigsa.com.mx','1504','Cordinacion de Proyectos de Desarrollo','2020-10-08','true','Villahermosa,Tab','1234','normal'),
(501698,'Morales Alonso Luis Enrique','luis.morales@sigsa.com.mx','1322','Cordinacion de Proyectos SIG','2021-02-16','true','Villahermosa,Tab','1234','normal'),
(501699,'Valenzuela Ulin Tenoch','tenoch.valenzuela@sigsa.com.mx','1322','Cordinacion de Proyectos SIG','2021-03-16','true','Villahermosa,Tab','1234','normal'),
(501701,'Cruz Quetzal Jorge Manuel','jorge.cruz@sigsa.com.mx','1322','Cordinacion de Proyectos SIG','2021-04-21','true','Villahermosa,Tab','1234','normal'),
(501705,'Ochoa Cetina Rodolfo','rodolfo.ochoa@sigsa.com.mx','1504','Cordinacion de Proyectos de Desarrollo','2021-05-04','true','Villahermosa,Tab','1234','normal'),
(501708,'Perez Jimenez Victor Fernando','victor.perez@sigsa.com.mx','1504','Cordinacion de Proyectos de Desarrollo','2021-06-07','true','Villahermosa,Tab','1234','normal'),
(501706,'Cruz Vazquez Jose Ivan','','1504','Cordinacion de Proyectos de Desarrollo','2021-06-07','true','Villahermosa,Tab','1234','normal'),
(501711,'Delgado Hernandez Azalia Del Carmen','azalia.hernandez@sigsa.com.mx','1504','Cordinacion de Proyectos de Desarrollo','2021-09-13','true','Villahermosa,Tab','1234','normal'),
(501710,'Tapia Mondragon Luis Antonio','luis.tapia@sigsa.com.mx','1322','Cordinacion de Proyectos SIG','2021-09-13','true','Villahermosa,Tab','1234','normal'),
(501712,'Solis Hernandez Pedro Reyez','pedro.hernandez@sigsa.com.mx','1322','Cordinacion de Proyectos SIG','2021-09-13','true','Villahermosa,Tab','1234','normal'),
(501713,'Ortiz Baldizon Alan Oswaldo','','1504','Cordinacion de Proyectos de Desarrollo','2021-09-20','true','Villahermosa,Tab','1234','normal'),
(501783,'Leon De La Cruz Lizbeth Alejandra','alejandra.leon@sigsa.com.mx','1568','Cordinacion Administrativa','2022-06-08','true','Villahermosa,Tab','1234','administrador'),
(501818,'Reyes Huerta Jose Enrique','jose.reyes@sigsa.com.mx','1504','Cordinacion de Proyectos de Desarrollo','2022-08-24','true','Villahermosa,Tab','1234','normal'),
(501819,'Chele Cuxim Jesus Gerardo','','1504','Cordinacion de Proyectos de Desarrollo','2022-08-24','true','Villahermosa,Tab','1234','normal'),
(501853,'Chi Chale Victor Andriw','victor.chi@sigsa.com.mx','1504','Cordinacion de Proyectos de Desarrollo','2023-05-21','true','Villahermosa,Tab','1234','normal'),
(501854,'Carrillo De LA Cruz Isai','isai.carrillo@sigsa.com.mx','1322','Cordinacion de Proyectos SIG','2023-05-21','true','Villahermosa,Tab','1234','normal');

SELECT*FROM empleados ORDER BY fecha_ingreso ASC
ALTER TABLE empleados RENAME COLUMN clave TO num_nomina
ALTER TABLE empleados DROP antiguedad

ALTER TABLE config_vacaciones2 RENAME COLUMN anios TO anios_servicio
SELECT * FROM config_vacaciones2

------------------------------------------------------------------------------------------------------------

CREATE TABLE solicitudes(
id SERIAL PRIMARY KEY,
num_nomina INTEGER REFERENCES empleados(num_nomina),
nombre VARCHAR,
email VARCHAR,
fecha_solicitud DATE,
fecha_inicio DATE,
fecha_fin DATE,
dias_solicitados INTEGER,
dias_restantes INTEGER,
fecha_reincorporacion DATE,
fecha_ingreso DATE,
dias_vacaciones INTEGER,
status VARCHAR
);

SELECT * FROM solicitudes

DROP TABLE solicitudes
DELETE FROM solicitudes;

INSERT INTO solicitudes (num_nomina,nombre,email, fecha_solicitud, fecha_inicio, fecha_fin, dias_solicitados,dias_restantes, fecha_reincorporacion,fecha_ingreso,dias_vacaciones,status)
VALUES (1331,'Alcudia Leon Juan Manuel','jalcudia@sigsa.info', '2023-10-19', '2023-10-20', '2023-11-20', 24,2,'2023-11-23','2006-12-14',26,'aceptado');


------------------------------------------------------------------------------------------------------------

CREATE TABLE config_vacaciones (
    anios_servicio INTEGER PRIMARY KEY,
    dias_vacaciones INTEGER
);
INSERT INTO config_vacaciones VALUES
(1,12),(2,14),(3,16),(4,18),(5,20),
(6,22),(7,22),(8,22),(9,22),(10,22),
(11,24),(12,24),(13,24),(14,24),(15,24),
(16,26),(17,26),(18,26),(19,26),(20,26),
(21,28),(22,28),(23,28),(24,28),(25,28),
(26,30),(27,30),(28,30),(29,30),(30,30),
(31,32),(32,32),(33,32),(34,32),(35,32)

SELECT*FROM config_vacaciones

ALTER TABLE config_vacaciones2 RENAME TO config_vacaciones;
