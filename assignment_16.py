#1. Create tables

import pymysql


try:
    connection = pymysql.connect(host='localhost', database='demo', user='helpme')
    print(connection)

finally:
    connection.close()
    print('Done!!')


import pymysql as pm

try:
    con = pm.connect(host='localhost', database='demo', user='helpme')

    cursor = con.cursor()

    query = 'create table zipcode(zipcode_id int(10) primary key,city varchar(20),state varchar(20),zcode varchar(20))'

    cursor.execute(query)

    query = 'create table publishers(p_id int(10) primary key,name varchar(20),street_add varchar(20),zipcode_id int(10),' \
            'FOREIGN KEY (zipcode_id) REFERENCES  zipcode(zipcode_id))'

    cursor.execute(query)

    query = 'create table title(title_id int(10) primary key,title varchar(20), isbn varchar(20), p_id int(10),' \
            'FOREIGN KEY (p_id) REFERENCES publishers(p_id))'
    cursor.execute(query)

    query = 'create table books(book_id int(10),title_id int(10),FOREIGN KEY (title_id) REFERENCES title(title_id),location varchar(20))'




    query = 'create table authors(a_id int(10) primary key,fname varchar(20),lastname varchar(20))'
    cursor.execute(query)

    print('Table created successfully!!')

    query = 'create table authors_titles(a_t_id int(10) primary key,a_id int(10),FOREIGN KEY (a_id) REFERENCES authors(a_id),title_id int(10),FOREIGN KEY(title_id) REFERENCES title(title_id))'

    cursor.execute(query)

    print('Table created successfully!!')


except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')


#2.Insert into the tables

import pymysql as pm
try:
    con = pm.connect(host='localhost', database='demo', user='helpme')

    cursor = con.cursor()

    query = "insert into zipcode(zipcode_id, city, state, zcode) \
    values(%s, %s, %s, %s)"

    records = [(10, 'Faridabad', 'Haryana', '23000'),
               (20, 'Patiala', 'Punjab', '20000')]

    cursor.executemany(query, records)
    con.commit()
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')


#3 Update the tables

import pymysql as pm

try:
    con = pm.connect(host='localhost', database='demo', user='helpme')

    cursor = con.cursor()

    query = "update zipcode set city='Rajpura' where city = 'Patiala'"

    cursor.execute(query)

    con.commit()

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')
