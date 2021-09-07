/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

CREATE TABLE territories (
    territory_id varchar(20) NOT NULL,
    territory_description varchar(1000) NOT NULL,
    region_id smallint NOT NULL
)