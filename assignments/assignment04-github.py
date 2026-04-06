# assignment04-github.py
# This program will read a file from a GitHub repository, modify its contents, and then update the file
# Author: Zoe McNamara Harlowe

from github import Github
from config import config as cfg
import requests
import re

apikey = cfg["githubkey"]

# Github API authentication
g = Github(apikey)

# Get a specific repo
repo = g.get_repo("zoeharlowe/test")

# Get the download URL for a file in the repo
file_info = repo.get_contents("assignment.txt")
file_url = file_info.download_url

# Get the content of the file
response = requests.get(file_url)
file_contents = response.text

# Replace "Andrew" for "Zoe" in file contents
updated_contents = re.sub(r"andrew", "Zoe", file_contents, flags=re.IGNORECASE)
print (updated_contents)

# Update the file with the new contents
commit_message = "Replace 'Andrew' with 'Zoe' via script"

update_response = repo.update_file(
    file_info.path,
    commit_message,
    updated_contents,
    file_info.sha
)

print(update_response)
