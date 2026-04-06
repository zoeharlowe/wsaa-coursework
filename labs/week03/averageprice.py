# averageprice.py
# This program calculates the average price of a list of books retrieved from an API.
# Author: Zoe McNamara Harlowe

from bookdao import readbooks

books = readbooks()

# find total price and number of books
total = 0
count = 0
for book in books:
    if 'price' in book and isinstance(book['price'], (int, float)):
        total += book['price']
        count += 1

print(f"Total price of all books: {total}")
print(f"Number of books: {count}")

average_price = total / count if count > 0 else 0

print(f"Average price of books: {average_price}")
