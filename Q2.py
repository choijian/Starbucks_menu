import pymysql
import pandas as pd
from tabulate import *
from db_password import password

tabulate.WIDE_CHARS_MODE = False


conn = password()
cur = conn.cursor()

cur.execute("SET GLOBAL log_bin_trust_function_creators = 1;")

#Procedure that print average price of drinks where category id is One
def execute_Q2_queries():
    print("\nProcedure that print average price of drinks where category id is One\n")
    cur.execute("DROP PROCEDURE IF EXISTS avg_price;")
    cur.execute("""
    create procedure avg_price(category_id varchar(5))
    begin
	    declare price_avg integer;
        select avg(price) into price_avg from size where size.category_id = category_id;
        drop table if exists avg_price;
        create table avg_price(
		    avg_price int,
		    category_id varchar(5)
	    );
        INSERT INTO avg_price(avg_price, category_id) VALUE (price_avg, category_id);
        select * from avg_price;
    end""")
    cur.callproc('avg_price', "1")
    row = cur.fetchall()
    x = pd.DataFrame(row)
    x.columns = ["avg_price ", "category_id"]
    print(tabulate(x,headers='keys',tablefmt = 'pretty', showindex = False, numalign='left'))
    print("")

#Function that counts the number of drinks where category_id is One
    print("\nFunction that counts the number of drinks where category_id is One\n")
    cur.execute("DROP FUNCTION IF exists drink_count;")
    cur.execute("""
    
    create function drink_count(category_id varchar(5)) returns integer
        begin
	        declare d_count integer;
                select count(*) into d_count from drinks where drinks.category_id = category_id;
                return d_count;
        end """)
    cur.execute("select drink_count(1)")
    row = cur.fetchall()
    x = pd.DataFrame(row)
    x.columns = ["Number of drinks where category_id is one"]
    print(tabulate(x,headers='keys',tablefmt = 'pretty', showindex = False, numalign='center'))
    print("")