# json.py
# Reads in a CSV file and outputs data as a list
# Author: Zoe McNamara Harlowe

import csv

FILENAME = "data.csv"
DATADIR = "../week01/"

linecount = 0

with open(DATADIR + FILENAME, "r") as fp:
    reader = csv.reader(fp, delimiter=',')
    for line in reader:
        if not linecount:
            print(f"{line}\n----------------------------")
        else:
            print(line)
        linecount += 1
    
    # Now find average age from the data
    ages = []
    linecount = 0
    fp.seek(0)  # Reset file pointer to the beginning

    for line in reader:
        if not linecount:
            linecount += 1
            continue  # Skip header line
        age = line[1]  # age is the second column
        ages.append(age)
        linecount += 1
    
    print(f"Ages: {ages}")

ages = list(map(int, ages))  # Convert string ages to integers

avg_age = sum(ages) / len(ages)

print(f"Average age: {avg_age}")