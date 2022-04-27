print("\033c")
import arxiv
from datetime import datetime, timezone
import logging
import string

logging.basicConfig(level=logging.INFO)

categories = [
    "cond-mat.mes-hall",
    "cond-mat.str-el",
    "cond-mat.stat-mech",
    "cond-mat.supr-con"
]

keywords = [
    'hydrodynamic',
    '"effective field theory"',
    'kinetic theory',
    'quasiparticle'
]

authors = [
    '"Rahul Nandkishore"',
    '"Andrew Lucas"',
    '"Thomas Scaffidi"',
    '"Paolo Glorioso"',
    '"Sean Hartnoll"'
    ]

def makelist(list):
    query = ""
    for item in list:
        query = query+ " OR " + item

    query = query[3:]
    return query


search_authors = arxiv.Search(
    query = "cat:({}) AND (au:({}))".format(
        makelist(categories),
        makelist(authors)
    ),
    sort_by=arxiv.SortCriterion.SubmittedDate
    )

search_keywords = arxiv.Search(
    query = "cat:({}) AND (all:({}))".format(
        makelist(categories),
        makelist(keywords)
    ),
    sort_by=arxiv.SortCriterion.SubmittedDate
    )


now = datetime.now(timezone.utc)

papers = []
with open("index.html", "w") as f:

    with open("head.html","r") as g:
        for line in g.readlines():
            f.write(line + "\n")

    # authors
    f.write("<h2>Followed Authors:</h2>\n")
    for result in search_authors.results():
        diff = now - result.published
        hrs = diff.total_seconds()/3600

        # Stop if the
        if hrs > 24:
            break

        print(result.title)
        print(result.published.date())
        print("")


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

    # Keywords
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



