/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE orders
    ADD CONSTRAINT fk_orders_employees FOREIGN KEY (employee_id) REFERENCES employees;