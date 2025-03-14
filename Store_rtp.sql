CREATE DATABASE IF NOT EXISTS Store_rtp;
SHOW DATABASES;
USE Store_rtp;

SHOW TABLES;

CREATE TABLE IF NOT EXISTS category(
   Id_category INT AUTO_INCREMENT,
   name VARCHAR(100) NOT NULL,
   PRIMARY KEY(Id_category)
);

CREATE TABLE IF NOT EXISTS product(
   Id_product INT AUTO_INCREMENT,
   name VARCHAR(100) NOT NULL,
   description TEXT,
   price DECIMAL(19,4) NOT NULL,
   quantity SMALLINT,
   Id_category INT NOT NULL,
   PRIMARY KEY(Id_product),
   FOREIGN KEY(Id_category) REFERENCES category(Id_category) ON DELETE CASCADE
);

INSERT INTO category (name) VALUES 
('Electronics'),
('Clothing'),
('Books');

INSERT INTO product (name, description, price, quantity, Id_category) VALUES
('Laptop', 'A high performance laptop', 999.99, 10, 1),
('T-Shirt', 'A comfortable cotton t-shirt', 19.99, 50, 2),
('Novel', 'A best-selling novel', 14.99, 30, 3);

DESCRIBE product;
SELECT * FROM product;

SELECT * FROM category WHERE name = 'Electronics' INNER JOIN product ON category.Id_category = product.Id_category;
