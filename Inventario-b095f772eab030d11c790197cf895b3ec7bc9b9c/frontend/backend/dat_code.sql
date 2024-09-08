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
    name_category VARCHAR(30));

create table produtos(
	id_produtos int auto_increment PRIMARY KEY,
	name_produtos varchar(30) not null,
    description_produtos TEXT,
    price_produtos int not null,
    quantity_produtos int not null,
    category_id INT DEFAULT ,
    Foreign Key (category_id) REFERENCES category(id_category)
);

CREATE TABLE logs_geral(
    id_logs   int AUTO_INCREMENT PRIMARY KEY,
    logs_text LONGTEXT
)

insert into logs_geral(logs_text) value ('teste_log')

INSERT into clients(gmail,ranking,password_client) VALUES('j@.com','clt','1')


SELECT * from clients