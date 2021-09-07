/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE employee_territories
    ADD CONSTRAINT fk_employee_territories_territories FOREIGN KEY (territory_id) REFERENCES territories;