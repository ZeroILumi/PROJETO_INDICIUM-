/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE employees
    ADD CONSTRAINT fk_employees_employees FOREIGN KEY (reports_to) REFERENCES employees;