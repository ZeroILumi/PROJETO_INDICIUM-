/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

CREATE TABLE region (
    region_id smallint NOT NULL,
    region_description varchar(1000) NOT NULL
)

INSERT INTO region VALUES (1, 'Eastern');
INSERT INTO region VALUES (2, 'Western');
INSERT INTO region VALUES (3, 'Northern');
INSERT INTO region VALUES (4, 'Southern');

ALTER TABLE region
    ADD CONSTRAINT pk_region PRIMARY KEY (region_id);

SELECT * FROM region