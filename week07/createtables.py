# createtables.py
# This program creates a table and populates it with data.
# Author: Zoe McNamara Harlowe

import pymysql
from config1 import config as cfg

connection = pymysql.connect(
    host="localhost",
    user="pythonuser",
    password="mypassword",
    database="wsaa"
)

cursor = connection.cursor()
sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
cursor.execute(sql)

cursor.close()
connection.close()
