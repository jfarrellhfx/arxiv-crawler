# imports
import os
from datetime import datetime, timedelta

# today and yesterday's date as strings
today = str(datetime.now().date())
yesterday = datetime.now() - timedelta(hours = 24)
yesterday = str(yesterday.date())

# move the previous index.html to the archive folder
os.system("mv index.html archive/{}-papers.html".format(yesterday))

# create the new list of papers
os.system("python arxiv-importer.py")

# update the website
os.system("git add .")
os.system('git commit -m "new day"')
os.system('git push origin main')