/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

ALTER TABLE territories
    ADD CONSTRAINT fk_territories_region FOREIGN KEY (region_id) REFERENCES region;