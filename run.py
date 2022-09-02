# imports
import os
from datetime import datetime, timedelta, timezone
from time import sleep

# today and yesterday's date as strings
yesterday = datetime.now(timezone.utc) - timedelta(hours = 24)
yesterday = str(yesterday.date())




# move the previous index.html to the archive folder
os.system("mv index.html archive/{}-papers.html".format(yesterday))

sleep(1) # wait a second

# Open an html file to hold links to all the old results.
with open("Archive.html", "w", encoding = "utf-8") as f:

    # add the header
    with open("head.html","r") as g:
        for line in g.readlines():
            f.write(line)

    # for every filename that starts with a sensible date in the 21st century, add a link to the corresponding page in the arxiv file.
    f.write("<body>")
    for name in sorted(os.listdir("archive"))[::-1]:
        if name[0] == "2":
            name2 = name[:10]
            f.write('<a href = "archive/{}">{}</a>\n'.format(name, name2))
            f.write("<br>\n")
    f.write("</body>")
    sleep(1)

    # create the new list of papers
    os.system("python arxiv-importer-v2.py")
