import pymysql
from db_password import password


conn = password()
cur = conn.cursor()

def create_tables():
    cur.execute('''create table if not exists category(
    category_id varchar(5) primary key,
    category_name varchar(10) not null
    );''')
    cur.execute("""create table if not exists drinks(
    drinks_id varchar(5) primary key,
    drinks_name varchar(10) not null,
    category_id varchar(5),
    is_new int not null,
    is_coffee int not null,
    foreign key (category_id) references category(category_id)
    );""")
    cur.execute("""create table if not exists nutrition(
    drinks_id varchar(5),
    category_id varchar(5),
    calorie int,
    natrium int,
    saturated_fat int,
    sugars int,
    protein int,
    caffeine int,
    foreign key (drinks_id) references drinks(drinks_id),
    foreign key (category_id) references drinks(category_id)
    );""")
    cur.execute("""create table if not exists drink_allergies(
    drinks_id varchar(5),
    category_id varchar(5),
    allergies_info varchar(10),
    foreign key (drinks_id) references drinks(drinks_id),
    foreign key (category_id) references drinks(category_id)
    );""")
    cur.execute("""create table if not exists size(
    drinks_id varchar(5),
    category_id varchar(5),
    oz int,
    price int,
    foreign key (drinks_id) references drinks(drinks_id),
    foreign key (category_id) references drinks(category_id)
    );""")
    cur.execute("""create table if not exists img(
    img_id varchar(5) primary key,
    drinks_id varchar(5),
    category_id varchar(5),
    img_url char(255),
    foreign key (drinks_id) references drinks(drinks_id),
    foreign key (category_id) references drinks(category_id)
    );""")
    cur.execute("""create table if not exists drink_des(
    drinks_id varchar(5),
    category_id varchar(5),
    des char(255),
    foreign key (drinks_id) references drinks(drinks_id),
    foreign key (category_id) references drinks(category_id)
    );""")
