"""
Jack Farrell, 2022

Using Arxiv API to search for papers with certain categories, authors, and keywords
"""

# Imports
print("\033c")
import arxiv
import os
from datetime import datetime, timezone, timedelta
import logging
import string
import codecs

# Set up logging for console output
logging.basicConfig(level=logging.INFO)

# Lists of categories, keywords, and authors to search
categories = [
    "cond-mat.mes-hall",
    "cond-mat.str-el",
    "cond-mat.stat-mech",
    "cond-mat.supr-con"
]

keywords = [
    'hydrodynamic',
    'hydrodynamics',
    '"effective field theory"',
    '"kinetic theory"',
    '"active matter"',
    'active'
]

authors = [
    '"Rahul Nandkishore"',
    '"Andrew Lucas"',
    '"Thomas Scaffidi"',
    '"Paolo Glorioso"',
    '"Sean Hartnoll"'
    ]


# period
period = 24


# helper function: given a list of keywords, put them into a long string separated by "OR" to use in the Arxiv API.
def makelist(list):
    query = ""
    for item in list:
        query = query+ " OR " + item

    query = query[3:]
    print(query)
    return query

# search arxiv for category and authors
search_authors = arxiv.Search(
    query = "cat:({}) AND (au:({}))".format(
        makelist(categories),
        makelist(authors)
    ),
    max_results=float('inf'),
    sort_by=arxiv.SortCriterion.SubmittedDate
    )

search_all = arxiv.Search(
    query = "cat:({})".format(
        makelist(categories)
    ),
    max_results=float('inf'),
    sort_by=arxiv.SortCriterion.SubmittedDate
    )


# arxiv for category and keywords
search_keywords = arxiv.Search(
    query = "cat:({}) AND (all:({}))".format(
        makelist(categories),
        makelist(keywords)
    ),
    max_results=float('inf'),
    sort_by=arxiv.SortCriterion.SubmittedDate
    )




# the time
now_utc = datetime.now(timezone.utc)
#now_utc = datetime(year=2022,month=8,day=31,hour=22,minute = 5).replace(tzinfo=timezone.utc)
now_est = now_utc - timedelta(hours = 4)
print("time")


def good_results(allresults):
    goodresults = []

    # what to do on tuesday, wednesday, thursday
    if now_est.weekday() in [1,2,3]:
        print("weekday")
       
        for result in allresults:
            print(result.published.tzinfo)
            print("")
            diff = now_utc- result.published
            hrs = diff.total_seconds() / 3600
            if hrs >= 2 and hrs <= 30:
                goodresults.append(result)
                 
            if hrs > 100:
                break

    elif now_est.weekday() == 6:
        print("SUNDAY!!")
        for result in allresults:
            diff = now_utc- result.published
            hrs = diff.total_seconds() / 3600
            if hrs >= 50 and hrs <= 78:
                goodresults.append(result)
            if hrs > 100:
                break
    elif now_est.weekday() == 0:
        print("monday")
        for result in allresults:
            diff = now_utc- result.published
          
            hrs = diff.total_seconds() / 3600
            if hrs >= 2 and hrs <= 78:
                goodresults.append(result)
            if hrs >= 100:
                break
    return goodresults



        



# create a html file to which to put the results
with open("index.html", "w", encoding="utf-8") as f:

    # add the header, which is stored in a different file
    with open("head.html","r") as g:
            for line in g.readlines():
                f.write(line)
    f.write("<body>\n")


   

        



        # authors ---------------------------------------------------

    # title
    f.write("<h2>Followed Authors:</h2>\n")
    try:
        # iterate through results
        for result in good_results(search_authors.results()):
            
            
            # format everyhthing nicely with links
            print(result.title)
            
            f.write("<h3>{}</h3>\n".format(result.title))
            f.write("<a href = \"{}\" target = \"_blank\">{}</a>\n<br>\n".format(result.links[0], result.links[0]))

            authors = ""
            for author in result.authors:
                name = author.name
                authors = authors + ", " + name.encode("ascii", errors = "ignore").decode()
                if authors[0] == ",":
                    authors = authors[2:]

            f.write("<i>{}</i>\n".format(authors))
            f.write("<br>\n")
            f.write("{}\n".format(result.summary))
            f.write("<br>\n")
            f.write("<br>\n")
    except: pass

    # Keywords ------------------------------------------------------------------
    # ditto everything from the authors...
    try:
        f.write("<h2>Keywords:</h2>\n")
        for result in good_results(search_keywords.results()):
            

            print(result.title)
            print(result.published)
            print("")
            f.write("<h3>{}</h3>\n".format(result.title))
            f.write("<a href = \"{}\" target = \"_blank\">{}</a>\n<br>\n".format(result.links[0], result.links[0]))

            authors = ""
            for author in result.authors:
                name = author.name
                authors = authors + ", " + name.encode("ascii", errors = "ignore").decode()
                if authors[0] == ",":
                    authors = authors[2:]

            f.write("<i>{}</i>\n".format(authors))
            f.write("<br>\n")
            f.write("{}\n".format(result.summary))
            f.write("<br>\n")
            f.write("<br>\n")
    except: pass



    f.write("<h2>All Papers:</h2>\n")
    try:
        for result in good_results(search_all.results()):
            print(result.published.time())
            print(result.title)
            print(result.published.date())
            print("")


            f.write("<h3>{}</h3>\n".format(result.title))
            f.write("<a href = \"{}\" target = \"_blank\">{}</a>\n<br>\n".format(result.links[0], result.links[0]))

            authors = ""
            for author in result.authors:
                name = author.name
                authors = authors + ", " + name.encode("ascii", errors = "ignore").decode()
                if authors[0] == ",":
                    authors = authors[2:]

            f.write("<i>{}</i>\n".format(authors))
            f.write("<br>\n")

            f.write("{}\n".format(result.summary))
            f.write("<br>\n")
            f.write("<br>\n")
    except: pass

    f.write("</body>")


