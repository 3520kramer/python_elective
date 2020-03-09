""" In this exercise you should read the content of your own github account api. 
    The url for this is https://api.github.com/users/<your-username>/repos
    
    1. Get all urls for all repositories on your account. 
    Clone all these repositories to your local computer. 

    2. Change your program into being able to "ask for" a username for any github account.
    Clone all repos from this users account. 

    3. If you did not already modualize your application do it now. 


"""

import os, requests, subprocess

username = input('Which user do you want to download from? ')

# gets the full api from specified url
res = requests.get('https://api.github.com/users/' + username + '/repos')

# saves it in json format
json_res = res.json()

# saves the length of the json file to find how many repos
json_length = len(json_res)

# creates list to save url's to clone from and saves each url in the json_res in the list
clone_url = []
for i in range(json_length):
    clone_url.append(json_res[i]['clone_url'])

print(clone_url)

# creates folder to save cloned url and change into it
os.mkdir('cloned_repos')
os.chdir('cloned_repos')

# run the command to clone the repos
for url in clone_url:
    subprocess.run(['git', 'clone', url])