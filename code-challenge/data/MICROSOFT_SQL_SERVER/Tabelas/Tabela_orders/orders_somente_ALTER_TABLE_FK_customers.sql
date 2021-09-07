/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE orders
    ADD CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES customers;