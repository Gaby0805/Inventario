-- Active: 1725058196579@@localhost@3306@estoque_produtos
CREATE DATABASE estoque_produtos


use estoque_produtos


CREATE TABLE clients(
	id_clients integer auto_increment PRIMARY KEY,
    gmail varchar(30),
    ranking ENUM('adm','clt'),
    password_client varchar(20)
);

create table product(
	id_product int auto_increment PRIMARY KEY,
	name_produts varchar(30) not null,
    description_produts varchar(60),
    price_product int not null,
    quantity_produts int not null,
    category_id INT,
    Foreign Key (category_id) REFERENCES category(id_category)
);



CREATE TABLE category(
    id_categoy int AUTO_INCREMENT PRIMARY KEY,
    name_category VARCHAR(30) not null,
    product_id int,
    Foreign Key (product_id) REFERENCES produtos(id_product)
    ); 

CREATE TABLE logs_geral(
    id_logs int PRIMARY KEY,
    logs_text LONGTEXT
)

SELECT * from estoque_produtos.clients

INSERT into estoque_produtos.clients (gmail,ranking, password_client) VALUES('gabriel', 'adm', '123')

