import os
from datetime import datetime, timedelta

today = str(datetime.now().date())
yesterday = datetime.now() - timedelta(hours = 24)
yesterday = str(yesterday.date())

os.system("mv index.html archive/{}-papers.html".format(yesterday))

os.system("python arxiv-importer.py")
os.system("git add .")
os.system('git commit -m "new day"')
os.system('git push origin main')