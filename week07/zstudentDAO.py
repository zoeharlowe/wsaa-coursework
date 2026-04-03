# studentDAO.py
# This program defines a Data Access Object (DAO) for the student table.
# Author: Zoe McNamara Harlowe

import pymysql
from config1 import config as cfg

class studentDAO:
    def __init__(self):
        self.host = cfg["host"]
        self.user = cfg["user"]
        self.password = cfg["password"]
        self.database = cfg["database"]
        self.db = None
        self.cursor = None

    def getcursor(self):
        self.db = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor()
        return self.cursor
    
    def closeall(self):
        self.cursor.close()
        self.db.close()

    def getall(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        rows = cursor.fetchall()
        self.closeall()

        return [
            {"id": row[0], "name": row[1], "age": row[2]}
            for row in rows
        ]
    
    def create(self, values):
        cursor = self.getcursor()
        sql = """
            INSERT INTO student (name, age)
            VALUES (%(name)s, %(age)s)
        """
        cursor.execute(sql, values)
        self.db.commit()
        newid = cursor.lastrowid
        self.closeall()
        return newid
    
    def findbyid(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM student WHERE id = %s"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        self.closeall()

        if row:
            return {"id": row[0], "name": row[1], "age": row[2]}
        return None
    
    def update(self, id, values):
        cursor = self.getcursor()
        sql = """
            UPDATE student
            SET name = %(name)s, age = %(age)s
            WHERE id = %(id)s
        """
        values["id"] = id
        cursor.execute(sql, values)
        self.db.commit()
        self.closeall()


    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM student WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
        self.closeall()
        return True
    
studentDAO = studentDAO()