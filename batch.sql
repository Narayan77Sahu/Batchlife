use bachelor_life;
create database bachelor_life;
create table user (id int,name varchar(50),email varchar(120),phone_no int(10));
create table rentals (id int ,title VARCHAR(120) NOT NULL,location VARCHAR(120) NOT NULL,monthly_rent INT NOT NULL,description VARCHAR(255),
available TINYINT(1) DEFAULT 1);
alter table rentals modify id int primary key auto_increment;
create table essentials (id int primary key auto_increment, item varchar(120) not null,price int not null,in_stock int not null default 0);
create table food (id int primary key auto_increment, name varchar(120) not null,type enum('veg','non-veg','mixed') not null,
  price int not null,description varchar(255));
create table orders (id int primary key auto_increment,user_id int not null,category enum('rental','food','essential') not null,
  item_id int not null,status enum('pending','confirmed','delivered','cancelled') default 'pending',
  created_at timestamp default current_timestamp,foreign key (user_id) references user(id));
insert into user (name, email, phone_no) values('demo user','demo@example.com','9876543210')on duplicate key update email=email;
alter table user modify phone_no varchar(15);
insert into rentals (title, location, monthly_rent, description, available) values
('1bhk near Jagamara', 'bhubaneswar - Jagamara', 7000, 'max-3 person ,semi-furnished, 1.5km from ITER', 1),
('shared room', 'bhubaneswar - patia', 3500, '2 sharing, wi-fi included', 1);

insert into food (name, type, price, description) values('veg meal', 'veg', 70, 'dalfry, mix-veg, roti, rice, salad'),
('chicken combo', 'non-veg', 120, 'chicken curry, roti, rice,salad');

insert into essentials (item, price, in_stock) values('single bed', 3000, 10),('mini fridge', 6500, 3),('chair', 600, 20),
('study table', 1650, 8);
