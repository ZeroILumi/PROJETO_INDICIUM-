/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

CREATE TABLE us_states (
    state_id smallint NOT NULL,
    state_name varchar(100),
    state_abbr varchar(2),
    state_region varchar(50)
)