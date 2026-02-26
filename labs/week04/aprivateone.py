# apriveateone.py
# This script demonstrates how to use a private GitHub API key stored in a separate configuration file
# Author: Zoe McNamara Harlowe

import requests
import json
from config import config2 as cfg
import base64

apiKey = cfg["htmltopdfkey"]
filename = "aprivateone.json"

url = "https://api.github.com/repos/zoeharlowe/aprivateone"

# Get repo information
response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)

    print("Status code:", response.status_code)

# Create a new file in the repository
url = "https://api.github.com/repos/zoeharlowe/aprivateone/contents/newfile.txt"

content = "Hello from the GitHub API!"
encoded = base64.b64encode(content.encode()).decode()

data = {
    "message": "Add newfile.txt via API",
    "content": encoded
}

headers = {
    "Authorization": f"token {apiKey}",
    "Accept": "application/vnd.github+json"
}

response = requests.put(url, headers = headers, json=data)
print(response.json())
