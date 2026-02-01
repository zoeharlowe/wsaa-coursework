# bankholidays.py
# This script fetches bank holiday data from the UK government website and prints it in JSON format.
# Author: Zoe McNamara Harlowe

# couldn't get this working

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)
