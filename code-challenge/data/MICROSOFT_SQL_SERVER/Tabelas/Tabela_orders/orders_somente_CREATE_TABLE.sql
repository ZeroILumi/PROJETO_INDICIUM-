/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

CREATE TABLE orders (
    order_id smallint NOT NULL,
    customer_id varchar(100),
    employee_id smallint,
    order_date date,
    required_date date,
    shipped_date date,
    ship_via smallint,
    freight real,
    ship_name varchar(40),
    ship_address varchar(60),
    ship_city varchar(15),
    ship_region varchar(15),
    ship_postal_code varchar(10),
    ship_country varchar(15)
)