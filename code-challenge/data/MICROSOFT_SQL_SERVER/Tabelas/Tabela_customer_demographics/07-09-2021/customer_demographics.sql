/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

CREATE TABLE customer_demographics (
    customer_type_id varchar(100) NOT NULL,
    customer_desc text
)

ALTER TABLE customer_demographics
    ADD CONSTRAINT pk_customer_demographics PRIMARY KEY (customer_type_id);