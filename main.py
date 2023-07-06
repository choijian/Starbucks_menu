import pymysql
from table_creating import create_tables
from values_inserting import insert_values
from Q1 import execute_Q1_queries
from Q2 import execute_Q2_queries
from Q3 import *
from db_password import password

conn = password()
cur = conn.cursor()

cur.execute("""drop table category,drinks,drink_allergies,nutrition,size,img,drink_des;""")
create_tables()     #Function for creating tables
insert_values()     #Function for inserting values
execute_Q1_queries()    #File call for q1 query
execute_Q2_queries()    #File call for q2 query

#loop to display q3 query
x = ''
while(x != 'q'):
    print_option()
    x = input("command(명령어 입력): ")
    main_table(x)