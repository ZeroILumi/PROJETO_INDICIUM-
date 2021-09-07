/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE employee_territories
    ADD CONSTRAINT fk_employee_territories_employees FOREIGN KEY (employee_id) REFERENCES employees;