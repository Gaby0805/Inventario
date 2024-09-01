-- Active: 1725058196579@@localhost@3306
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
    client_id INT,
    Foreign Key (client_id) REFERENCES clients(id_client)
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
