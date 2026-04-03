# create.py
# This program creates data in a table.
# Author: Zoe McNamara Harlowe

import pymysql

db = pymysql.connect(
    host="localhost",
    user="pythonuser",
    password="mypassword",
    database="wsaa"
)

# insert data
cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)

cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
cursor.close()
db.close()
