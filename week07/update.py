# update.py
# This program updates data in a table.
# Author: Zoe McNamara Harlowe

import pymysql

db = pymysql.connect(
    host="localhost",
    user="pythonuser",
    password="mypassword",
    database="wsaa"
)

cursor = db.cursor()
sql="update student set name= %s, age=%s where id = %s"
values = ("Joe",33, 1)
cursor.execute(sql, values)
db.commit()
print("update done")
cursor.close()
db.close()
