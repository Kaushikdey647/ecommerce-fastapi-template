-- POSTGRESQL ONE TIME DATABASE INITIATION SCRIPT

-- SOME HANDLERS MIGHT NEED IT, SOME BUILD SCHEMA THEMSELVES

-- CREATOR: KAUSHIK DEY (kaushikdey647@gmail.com)

-- DATE: 18/04/2023

-- CREATE A ROLE TO HANDLE THE DATABASE

create user "backend_db_admin" with password "auth123";

-- CREATE A DATABASE

create database "backend_db";

-- GRANT ALL PRIVILEGES ON DATABASE "backend_db" TO "backend_db_admin"

grant all privileges on database "backend_db" to "backend_db_admin";

-- SWITCH TO THE NEWLY CREATED ROLE

\c backend_db

-- START CREATING TABLES

-- order_status(*status_id, status_name)

create table order_status (
    status_id serial primary key,
    status_name varchar(20) not null
);

-- order(*order_id, user_id, date, total_cost, payment_id, status_id)

create table order (
    order_id serial primary key,
    user_id int not null,
    date date not null,
    total_cost float not null,
    payment_id int not null,
    status_id int not null
);

-- payment(*payment_id, user_id, card_number, card_holder, expiration_date, cvv)

create table payment (
    payment_id serial primary key,
    user_id int not null,
    card_number varchar(16) not null,
    card_holder varchar(50) not null,
    expiration_date date not null,
    cvv int not null
);

-- user_data(*user_id, name, email, password)

create table user_data (
    user_id serial primary key,
    name varchar(50) not null,
    email varchar(50) not null,
    password varchar(50) not null
);

-- cart(*cart_id, user_id, product_id, quantity)

create table cart (
    cart_id serial primary key,
    user_id int not null,
    product_id int not null,
    quantity int not null
);

-- product(*product_id, name, description, price, image_url)

create table product (
    product_id serial primary key,
    name varchar(50) not null,
    description varchar(200) not null,
    price float not null,
    image_url varchar(200) not null
);

-- category(*category_id, name)

create table category (
    category_id serial primary key,
    name varchar(50) not null
);

-- customer_service(*inquiry_id, user_id, date, message)

create table customer_service (
    inquiry_id serial primary key,
    user_id int not null,
    date date not null,
    message varchar(200) not null
);

-- create references now

-- order

alter table order
add constraint fk_order_user_id
foreign key (user_id) references user_data (user_id);

alter table order
add constraint fk_order_payment_id
foreign key (payment_id) references payment (payment_id);

alter table order
add constraint fk_order_status_id
foreign key (status_id) references order_status (status_id);

-- payment

alter table payment
add constraint fk_payment_user_id
foreign key (user_id) references user_data (user_id);

-- cart

alter table cart
add constraint fk_cart_user_id
foreign key (user_id) references user_data (user_id);

alter table cart
add constraint fk_cart_product_id
foreign key (product_id) references product (product_id);

-- customer_service

alter table customer_service
add constraint fk_customer_service_user_id
foreign key (user_id) references user_data (user_id);