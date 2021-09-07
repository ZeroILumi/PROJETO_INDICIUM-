/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE orders
    ADD CONSTRAINT fk_orders_shippers FOREIGN KEY (ship_via) REFERENCES shippers;