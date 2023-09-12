# FILL YOUR GITHUB HISTORY

# Log into your a github account 

# Generate a new SSH key https://docs.github.com/en/authentication/connecting-to-github-with-ssh
        # in terminal: ssh-keygen -t ed25519 -C "your_email@example.com"
        # name it something when it ask... like 'myKey'
        # just hit enter for password
        # it will create 2 files: myKey and myKey.pub - move them to /Users/jacobjelen/.ssh
        # edit /Users/jacobjelen/.ssh/config with text edit to look like this
                # Host github.com
                #         AddKeysToAgent yes
                #         UseKeychain yes
                #         IdentityFile ~/.ssh/myKey
                #         IgnoreUnknown UseKeychain

# open myKey.pub in textedit and copy everything in it (it's the public key)
        # you can also copy it in terminal: pbcopy < ~/.ssh/myKey.pub
# go to your https://github.com/settings/keys - click 'Add New SSH Key' 
# name it something and paste the public key in the second field and 'add'
# run this to start an ssh-agent in terminal: eval "$(ssh-agent -s)"
# you can now write to your github from your computer

# create a new repo, clone it from your command line and enter into it's folder
# copy this file into it
# change the variables to fit your account and needs

username = 'BjornHammars'
email = 'bjorn.hammars@gmail.com'
startDaysAgo = 300
endDaysAgo = 1
minCommitsPerDay = 0
maxCommitsPerDay = 2

# run this code in terminal: python3 app.py
# if there are no errors you should see your repo filled with commits

import os
from random import randint
from datetime import datetime, timedelta

# Get today's date
today = datetime.now()

os.system(f'git config --global user.name {username}')
os.system(f'git config --global user.email {email}')
os.system(f'git config user.name {username}')
os.system(f'git config user.email {email}')

# can do this manually instead
os.system('git add app.py')
os.system('git add pycode/app.py')

for i in range(endDaysAgo, startDaysAgo):
    mydate = today - timedelta(days=i)
    # formated = mydate.isoformat()
    formated = mydate.strftime('%Y-%m-%dT%H:%M:%S')
    # formated = formated[:21]

    print(formated)

    for j in range(0, randint(minCommitsPerDay, maxCommitsPerDay)):
        d = str(i) + ' days and '+ str(j)+' commits'
        with open('file.txt', 'w') as file:
                file.write(d)
        os.system('git add file.txt')
        os.system('git ignore app.py')
        
        cmd = f'GIT_AUTHOR_DATE={formated} GIT_COMMITTER_DATE={formated} git commit --author="{username} <{email}>" -m "{formated}"'
        os.system(cmd)        

os.system('git push -u origin main')
