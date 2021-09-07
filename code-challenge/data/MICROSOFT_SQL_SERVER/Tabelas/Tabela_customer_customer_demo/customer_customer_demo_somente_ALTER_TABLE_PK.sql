/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE customer_customer_demo
    ADD CONSTRAINT pk_customer_customer_demo PRIMARY KEY (customer_id, customer_type_id);