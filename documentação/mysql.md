CREATE DATABASE estoque;

CREATE TABLE clients(
	id integer auto_increment,
    name_client varchar(30),
    password_client varchar(20),
    primary key(id)
);
create table produtos (
	id_produts int auto_increment,
	name_produts varchar(30) not null,
    description_produts varchar(60),
    price_produts int not null,
    quantity_produts int not null,
	category_produts enum('brinquedos','armas','pessoas'),
    primary key(id_produts)
);

