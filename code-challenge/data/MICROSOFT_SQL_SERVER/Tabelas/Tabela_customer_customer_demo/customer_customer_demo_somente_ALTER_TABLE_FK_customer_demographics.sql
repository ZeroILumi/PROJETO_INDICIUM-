/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE customer_customer_demo
    ADD CONSTRAINT fk_customer_customer_demo_customer_demographics FOREIGN KEY (customer_type_id) REFERENCES customer_demographics;