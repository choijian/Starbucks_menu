import pymysql
import pandas as pd
from tabulate import *
from db_password import password

tabulate.WIDE_CHARS_MODE = False


conn = password()
cur = conn.cursor()

joined_table = "drinks natural join size natural join drink_des"

#for print dataframe
def print_df(df):
    x = pd.DataFrame(df)
    x.columns = ["drinks_id","category_id","drinks_name","is_new","is_coffee","oz","price","description"]
    print(tabulate(x,headers='keys',tablefmt = 'pretty', showindex = False, numalign='left'))


def print_option():
    print("")
    print("***사용 가능 명령어 리스트***")
    print("a  : 모든 메뉴 조회(all)")
    print("f  : 조건에 맞는 메뉴만 조회(find)")
    print("r  : 메뉴 정보 변경(revise)")
    print("q  : 저장하고 나가기(quit)")
    print("")

#function for showing all menu
def show_all_data():
    cur.execute("select * from {};".format(joined_table))
    row = cur.fetchall()
    x = pd.DataFrame(row)
    x.columns = ["drinks_id", "category_id", "drinks_name", "is_new", "is_coffee", "oz", "price", "des"]
    print(tabulate(x,headers='keys',tablefmt = 'pretty', showindex = False, numalign='left'))
    print("")
    #show_info = cur.fetchall()
    #print(pd.DataFrame(show_info))

#function for selecting only the menus that meet the condition
def search_data():
    print("무엇을 기준으로 검색하시겠습니까? (drinks_name/category_id/is_coffee/price)")
    n_con = input("> ")

#the case if the user wants to search through the menu name
    if n_con == 'drinks_name':
        d_name = str(input("이름을 입력하세요: "))
        sql = "select * from {} where drinks.drinks_name = '{}'".format(joined_table, d_name)
        cur.execute(sql)
        print_df(cur.fetchall())

#the case if the user wants to search through the category id
    elif n_con == 'category_id':
        c_id = str(input("enter category_id(1/2/3): "))
        sql = "select * from {} where drinks.category_id = {}".format(joined_table, c_id)
        cur.execute(sql)
        print_df(cur.fetchall())

#the case if the user wants to search through whether drinks is coffee or not
    elif n_con == 'is_coffee':
        i_c = str(input("whether coffee(1) or not(0): "))
        sql = "select * from {} where is_coffee = {}".format(joined_table, i_c)
        cur.execute(sql)
        print_df(pd.DataFrame(cur.fetchall()))

#the case if the user wants to search through price
    elif n_con == 'price':
        upper_boundary = int(input("enter upper_boundary: "))
        lower_boundary = int(input("enter lower_boundary: "))
        sql = "select * from {} where size.price between {} and {}".format(joined_table, lower_boundary, upper_boundary)
        cur.execute(sql)
        print_df(pd.DataFrame(cur.fetchall()))

#function for revising data, data can be selected only by drinks_id
def revised_data():
    print("※ 정보를 변경할 음료의 선택은 drinks_id를 통해서만 가능합니다.")
    d_id = input("drinks_id: ")
    sql = "SELECT * FROM {} WHERE drinks_id = '{}'".format(joined_table, d_id)
    cur.execute(sql)
    con = input("어떤 정보를 변경하시겠습니까(oz/price)? ")

#the case if user wants to change 'oz'
    if con == "oz":
        r_oz = input("oz to change: ")
        update_sql = "UPDATE size SET oz = '{}' where drinks_id = '{}'".format(r_oz, d_id)
        cur.execute(update_sql)
        r_sql = "SELECT * FROM {} WHERE size.oz = {}".format(joined_table,r_oz)
        cur.execute(r_sql)
        print("revised data:")
        print_df(pd.DataFrame(cur.fetchall()))

#the case if user wants to change 'price'
    elif con == "price":
        r_price = input("price to change: ")
        update_sql = "UPDATE size SET price = '{}' where drinks_id = '{}'".format(r_price, d_id)
        cur.execute(update_sql)
        r_sql = "SELECT * FROM {} WHERE size.price = {}".format(joined_table,r_price)
        cur.execute(r_sql)
        print("revised data:")
        print_df(pd.DataFrame(cur.fetchall()))

#main table where users can select options
def main_table(cmd):
    if (cmd == 'a'):
        show_all_data()
    elif cmd == 'f':
        search_data()
    elif cmd == 'r':
        revised_data()



