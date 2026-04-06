# messingwithrequests.py
# This program demonstrates how to use the requests library to make HTTP requests and handle responses.
# Zoe McNamara Harlowe

from urllib import response
from hyperlink import URL
import requests

url = "https://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    return response.json()

def readbook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)

    # check for correct response code
    print("Response status code:", response.status_code)
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
    print("Response status code:", response.status_code)

    try:
        return response.json()
    except ValueError:
        print("Server did not return JSON. Raw response:")
        print(response.text)
        return None

def updatebook(id, book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    print("Response status code:", response.status_code)

def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    print("Response status code:", response.status_code)
    return response.json()

if __name__ == "__main__":
    updatebook(1646, {"title": "Robinson Crusoe", "author": "Daniel Defoe", "price":12})
    print(readbook(1646))

