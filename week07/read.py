# read.py
# This program reads data from a table.
# Author: Zoe McNamara Harlowe

import pymysql

db = pymysql.connect(
    host="localhost",
    user="pythonuser",
    password="mypassword",
    database="wsaa"
)

# view data
cursor = db.cursor()
sql="select * from student where id = %s"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
 print(x)
cursor.close()
db.close()
