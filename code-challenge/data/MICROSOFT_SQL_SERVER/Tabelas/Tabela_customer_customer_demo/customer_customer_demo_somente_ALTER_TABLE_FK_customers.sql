/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE customer_customer_demo
    ADD CONSTRAINT fk_customer_customer_demo_customers FOREIGN KEY (customer_id) REFERENCES customers;