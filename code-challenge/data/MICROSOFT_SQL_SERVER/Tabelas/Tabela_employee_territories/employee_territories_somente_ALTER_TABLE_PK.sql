/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE employee_territories
    ADD CONSTRAINT pk_employee_territories PRIMARY KEY (employee_id, territory_id);