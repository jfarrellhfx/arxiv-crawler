# imports
import os
from datetime import datetime, timedelta

# today and yesterday's date as strings
today = str(datetime.now().date())
yesterday = datetime.now() - timedelta(hours = 24)
yesterday = str(yesterday.date())

# move the previous index.html to the archive folder
os.system("mv index.html {}-papers.html".format(yesterday))

# create the new list of papers
os.system("python arxiv-importer.py")

# update the website
os.system("git add .")
os.system('git config --global user.name "jfarrellhx"')
os.system('git config --global user.email "jfarrellhfx@gmail.com"')
os.system('git commit -m "new day"')
os.system('git push https://jfarrellhfx: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@arxiv-crawler.biz/file.git origin main ')
