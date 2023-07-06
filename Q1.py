import pymysql
import pandas as pd
from tabulate import *
from db_password import password

tabulate.WIDE_CHARS_MODE = False


conn = password()
cur = conn.cursor()

def execute_Q1_queries():
    #using 'WHERE'
    #print 'drink name' which has caffeine
    print("\nDrinks with caffeine")
    cur.execute("select drinks_name from drinks where is_coffee = 1;")
    row = cur.fetchall()
    x = pd.DataFrame(row)
    x.columns = ["drinks_name"]
    print(tabulate(x,headers='keys',tablefmt = 'pretty', showindex = False, numalign='left'))
    print("")

    #using from 'FROM' to call two tables
    #get all values from drink, drink_des table
    print("Drinks with drinks_description")
    cur.execute("select * from drinks, drink_des where drinks.drinks_id = drink_des.drinks_id;")
    row = cur.fetchall()
    x = pd.DataFrame(row)
    x.columns = ["drinks_id", "drinks_name", "category_id", "is_new", "is_coffee", "drinks_id", "category_id", "des"]
    print(tabulate(x,headers='keys',tablefmt = 'pretty', showindex = False, numalign='left'))
    print("")

    #using 'union' as a 'set function'
    #Load drinks with no caffeine and category_id is 1
    print("Drinks which are decaffeinated or cold_brew")
    cur.execute("(select * from drinks where is_coffee = 0) union (select * from drinks where category_id = 1);")
    row = cur.fetchall()
    x = pd.DataFrame(row)
    x.columns = ["drinks_id","drinks_name","category_id","is_new","is_coffee"]
    print(tabulate(x,headers='keys',tablefmt = 'pretty', showindex = False, numalign='left'))
    print("")

    #using group by + aggergate
    #print the maximum 'price' menu among categories
    print("the maximum 'price' menu among categories")
    cur.execute("""select category_name, size.category_id, avg(price)
    from category, size
    where category.category_id = size.category_id
    group by size.category_id;""")
    row = cur.fetchall()
    x = pd.DataFrame(row)
    x.columns = ["drinks_name ", "category_id", "price"]
    print(tabulate(x,headers='keys',tablefmt = 'pretty', showindex = False, numalign='left'))
    print("")