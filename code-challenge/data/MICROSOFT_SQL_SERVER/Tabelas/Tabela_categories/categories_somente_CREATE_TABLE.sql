/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium
CREATE TABLE categories (
    category_id smallint NOT NULL,
    category_name character varying(15) NOT NULL,
    description text,
    picture bit
)