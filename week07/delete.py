# delete.py
# This program deletes data from a table.
# Author: Zoe McNamara Harlowe

import pymysql

db = pymysql.connect(
    host="localhost",
    user="pythonuser",
    password="mypassword",
    database="wsaa"
)

cursor = db.cursor()

sql = "DELETE FROM student WHERE id = %s"
values = (1,)

cursor.execute(sql, values)
db.commit()
print("delete done")
cursor.close()
db.close()