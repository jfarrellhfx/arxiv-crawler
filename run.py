# imports
import os
from datetime import datetime, timedelta
from time import sleep

# today and yesterday's date as strings
today = str(datetime.now().date())
yesterday = datetime.now() - timedelta(hours = 24)
yesterday = str(yesterday.date())

# move the previous index.html to the archive folder
os.system("mv index.html {}-papers.html".format(yesterday))

sleep(1) # wait a second

# Open an html file to hold links to all the old results.
with open("Archive.html", "w") as f:

    # add the header
    with open("head.html","r") as g:
        for line in g.readlines():
            f.write(line + "\n")

    # for every filename that starts with a sensible date in the 21st century, add a link to the corresponding page in the arxiv file.
    for name in sorted(os.listdir("."))[::-1]:
        if name[0] == "2":
            name2 = name[:10]
            f.write('<a href = "{}">{}</a>\n'.format(name, name2))
            f.write("<br>\n")
    f.write("</body>")


# create the new list of papers
os.system("python arxiv-importer.py")

# github access token: needs to be broken up, because github doesn't like you to put the tokens inside of the repositories!
#
token1 = "ghp_Gomuk1hkXJLN9"
#
token2 = "Ik3mzWZu4YMEzuwSb4aM965"

# update the website
os.system("git add .")
os.system('git config --global user.name "jfarrellhx"')
os.system('git config --global user.email "jfarrellhfx@gmail.com"')
os.system('git commit -m "new day"')
os.system('git push https://jfarrellhfx:{}@github.com/jfarrellhfx/arxiv-crawler.git main'.format(token))
