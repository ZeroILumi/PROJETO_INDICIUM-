/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE products
    ADD CONSTRAINT fk_products_suppliers FOREIGN KEY (supplier_id) REFERENCES suppliers;