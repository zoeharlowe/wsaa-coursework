from github import Github
from labs.week04.config import config3 as cfg
import requests

apikey = cfg["githubkey"]

# List out the repositories
g = Github(apikey)
#for repo in g.get_user().get_repos():
 #print(repo.name)

# Get a specific repo
repo = g.get_repo("zoeharlowe/test")
#print(repo.clone_url)

# Get the download URL for a file in the repo
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# Get the content of the file
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

# Add new contents
newContents = contentOfFile + " more stuff \n hello"
#print (newContents)

# Update the file with the new contents
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)
