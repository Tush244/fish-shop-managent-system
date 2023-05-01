import sqlite3
def create_db():
    con=sqlite3.connect(database=r'TUSHARG244.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(emp_id INTEGER PRIMARY KEY,name text,email text,gender text,contact text,DOB text,DOJ text,pass text,utype text,address text,salary text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(supp_id INTEGER PRIMARY KEY,name text,contact text,desc text)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS f_category(cat_id INTEGER PRIMARY KEY,name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS f_product(p_id INTEGER PRIMARY KEY, category text,name text, QNT text,weight text, price text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(cust_id INTEGER PRIMARY KEY, name text,mobile text, address text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS stock(f_cat, f_name text,f_weight text, st_date text,st_price int)")
    con.commit()
create_db()