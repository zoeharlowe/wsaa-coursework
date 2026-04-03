# teststudentDAO.py
# This program tests the studentDAO class.
# Author: Zoe McNamara Harlowe

from zstudentDAO import studentDAO

student = {
    "name": "Mary",
    "age": 21
}

# create
studentid = studentDAO.create(student)

# find by id
result = studentDAO.findbyid(studentid)
print(result)

# update
newstudentvalues = {"name": "Fred", "age": 22}
studentDAO.update(studentid, newstudentvalues)

# find again
result = studentDAO.findbyid(studentid)
print(result)

# get all
print("test get all")
allstudents = studentDAO.getall()
print(allstudents)

# delete
studentDAO.delete(studentid)
print("test delete")
