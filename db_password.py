import pymysql

def password():
    conn = pymysql.connect(host = 'localhost', user = "root", password="abc0422", db = "starbucks_menu")
    return conn
