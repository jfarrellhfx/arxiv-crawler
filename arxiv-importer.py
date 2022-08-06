"""
Jack Farrell, 2022

Using Arxiv API to search for papers with certain categories, authors, and keywords
"""

# Imports
print("\033c")
import arxiv
import os
from datetime import datetime, timezone
import logging
import string

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
    '"Sean Hartnoll"',
    '"Ananth Kandala"'
    ]

# keep track of whether there are any results
good_results = 0

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
    sort_by=arxiv.SortCriterion.SubmittedDate
    )

search_all = arxiv.Search(
    query = "cat:({})".format(
        makelist(categories),
    ),
    sort_by=arxiv.SortCriterion.SubmittedDate
    )


# arxiv for category and keywords
search_keywords = arxiv.Search(
    query = "cat:({}) AND (all:({}))".format(
        makelist(categories),
        makelist(keywords)
    ),
    sort_by=arxiv.SortCriterion.SubmittedDate
    )

# the time
now = datetime.now(timezone.utc)

# create a html file to which to put the results
with open("index.html", "w") as f:

    # add the header, which is stored in a different file
    with open("head.html","r") as g:
        for line in g.readlines():
            f.write(line + "\n")

    # authors ---------------------------------------------------

    # title
    f.write("<h2>Followed Authors:</h2>\n")

    # iterate through results
    for result in search_authors.results():

        # figure out how long it's been since the result was published, and break the loop if this time is greater than 24 hrs.
        diff = now - result.published
        hrs = diff.total_seconds()/3600
        if hrs > 30 * 24:
            break

        # format everyhthing nicely with links
        print(result.title)
        print(result.published.date())
        print("")
        good_results += 1


        f.write("<body>\n")
        f.write("<h3>{}</h3>\n".format(result.title))
        f.write("<a href = \"{}\">{}</a>\n<br>\n".format(result.links[0], result.links[0]))

        authors = ""
        for author in result.authors:
            name = author.name
            authors = authors + ", " + name.encode("ascii", errors = "ignore").decode()
            if authors[0] == ",":
                authors = authors[2:]

        f.write("<i>{}</i>\n".format(authors))
        f.write("<br>\n")
        f.write("<br>\n")
        f.write("{}\n".format(result.summary))
        f.write("<br>\n")
        f.write("<br>\n")

    # Keywords ------------------------------------------------------------------
    # ditto everything from the authors...
    f.write("<h2>Keywords:</h2>\n")
    for result in search_keywords.results():
        diff = now - result.published
        hrs = diff.total_seconds()/3600

        # Stop if the
        if hrs > 24:
            break

        print(result.title)
        print(result.published.date())
        print("")
        good_results += 1


        f.write("<body>\n")
        f.write("<h3>{}</h3>\n".format(result.title))
        f.write("<a href = \"{}\">{}</a>\n<br>\n".format(result.links[0], result.links[0]))

        authors = ""
        for author in result.authors:
            name = author.name
            authors = authors + ", " + name.encode("ascii", errors = "ignore").decode()
            if authors[0] == ",":
                authors = authors[2:]

        f.write("<i>{}</i>\n".format(authors))
        f.write("<br>\n")
        f.write("<br>\n")
        f.write("{}\n".format(result.summary))
        f.write("<br>\n")
        f.write("<br>\n")
        f.write("<br>\n")
        f.write("<br>\n")

        f.write("</body>")


        f.write("<h2>All Papers:</h2>\n")
    for result in search_keywords.results():
        diff = now - result.published
        hrs = diff.total_seconds()/3600

        # Stop if the
        if hrs > 24:
            break

        print(result.title)
        print(result.published.date())
        print("")
        good_results += 1


        f.write("<body>\n")
        f.write("<h3>{}</h3>\n".format(result.title))
        f.write("<a href = \"{}\">{}</a>\n<br>\n".format(result.links[0], result.links[0]))

        authors = ""
        for author in result.authors:
            name = author.name
            authors = authors + ", " + name.encode("ascii", errors = "ignore").decode()
            if authors[0] == ",":
                authors = authors[2:]

        f.write("<i>{}</i>\n".format(authors))
        f.write("<br>\n")
        f.write("<br>\n")
        f.write("{}\n".format(result.summary))
        f.write("<br>\n")
        f.write("<br>\n")
        f.write("<br>\n")
        f.write("<br>\n")

        f.write("</body>")


