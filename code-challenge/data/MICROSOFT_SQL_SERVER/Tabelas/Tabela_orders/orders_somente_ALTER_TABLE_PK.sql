/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE orders
    ADD CONSTRAINT pk_orders PRIMARY KEY (order_id);