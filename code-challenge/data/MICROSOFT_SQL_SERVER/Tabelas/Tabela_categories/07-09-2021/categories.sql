/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium

CREATE TABLE categories (
    category_id smallint NOT NULL,
    category_name character varying(15) NOT NULL,
    description text,
    picture bit
)

INSERT INTO categories VALUES (1, 'Beverages', 'Soft drinks, coffees, teas, beers, and ales', '0');
INSERT INTO categories VALUES (2, 'Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings', '0');
INSERT INTO categories VALUES (3, 'Confections', 'Desserts, candies, and sweet breads', '0');
INSERT INTO categories VALUES (4, 'Dairy Products', 'Cheeses', '0');
INSERT INTO categories VALUES (5, 'Grains/Cereals', 'Breads, crackers, pasta, and cereal', '0');
INSERT INTO categories VALUES (6, 'Meat/Poultry', 'Prepared meats', '0');
INSERT INTO categories VALUES (7, 'Produce', 'Dried fruit and bean curd', '0');
INSERT INTO categories VALUES (8, 'Seafood', 'Seaweed and fish', '0');

ALTER TABLE categories
    ADD CONSTRAINT pk_categories PRIMARY KEY (category_id);

SELECT * FROM categories