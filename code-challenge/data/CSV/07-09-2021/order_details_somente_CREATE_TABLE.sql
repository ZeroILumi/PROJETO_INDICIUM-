/*CREATE DATABASE Projeto_Indicium*/
USE Projeto_Indicium
CREATE TABLE order_details
(
   order_id SMALLINT FOREIGN KEY REFERENCES orders(order_id),
   product_id SMALLINT FOREIGN KEY REFERENCES products(product_id),
   unit_price FLOAT NOT NULL,
   quantity INT NOT NULL,
   discount FLOAT NOT NULL,
   creation_date DATETIME NOT NULL
)
