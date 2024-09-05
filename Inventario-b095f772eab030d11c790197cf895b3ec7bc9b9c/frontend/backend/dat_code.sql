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
    category_id INT,
    Foreign Key (category_id) REFERENCES category(id_category)
);



CREATE TABLE logs_geral(
    id_logs int PRIMARY KEY,
    logs_text LONGTEXT
)

SELECT * from estoque_produtos.clients

SELECT  *  from produtos 

INSERT INTO estoque_produtos.clients(gmail, ranking, password_client ) VALUES ('b', "2", '456')

drop database estoque_produtos

INSERT into category(name_category) VALUE('2')

SELECT * from category

update produtos set name_produtos='augusto', description_produtos='sexo1', price_produtos=2, quantity_produtos=3, category_id=4 where id_produtos=1 
