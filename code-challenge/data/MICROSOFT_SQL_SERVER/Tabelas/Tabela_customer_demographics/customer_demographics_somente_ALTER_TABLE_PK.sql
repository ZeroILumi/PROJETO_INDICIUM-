/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE customer_demographics
    ADD CONSTRAINT pk_customer_demographics PRIMARY KEY (customer_type_id);