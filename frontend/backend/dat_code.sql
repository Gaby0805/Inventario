-- Active: 1725058196579@@localhost@3306@estoque_produtos
CREATE DATABASE estoque_produtos


use estoque_produtos


CREATE TABLE clients(
	id_clients integer auto_increment PRIMARY KEY,
    gmail varchar(30),
    ranking ENUM('adm','clt'),
    password_client varchar(20)
);

CREATE TABLE category(
    id_category int AUTO_INCREMENT PRIMARY KEY,
    name_category VARCHAR(30) not null,
    produtos_id int
    ); 

create table produtos(
	id_produtos int auto_increment PRIMARY KEY,
	name_produtos varchar(30) not null,
    description_produtos varchar(60),
    price_produtos int not null,
    quantity_produtos int not null,
    category_id INT,
    Foreign Key (category_id) REFERENCES category(id_category)
);



CREATE TABLE logs_geral(
    id_logs int PRIMARY KEY,
    logs_text LONGTEXT
)

    SELECT * from estoque_produtos.category

DROP DATABASE estoque_produtos