/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

CREATE TABLE customer_customer_demo (
    customer_id varchar(100) NOT NULL,
    customer_type_id varchar(100) NOT NULL
)

ALTER TABLE customer_customer_demo
    ADD CONSTRAINT pk_customer_customer_demo PRIMARY KEY (customer_id, customer_type_id);*/

ALTER TABLE customer_customer_demo
    ADD CONSTRAINT fk_customer_customer_demo_customer_demographics FOREIGN KEY (customer_type_id) REFERENCES customer_demographics;

ALTER TABLE customer_customer_demo
    ADD CONSTRAINT fk_customer_customer_demo_customers FOREIGN KEY (customer_id) REFERENCES customers;
