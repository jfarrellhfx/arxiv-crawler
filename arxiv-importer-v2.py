import requests
from bs4 import BeautifulSoup

page = requests.get("https://arxiv.org/list/cond-mat/new")
soup = BeautifulSoup(page.content, 'html.parser')
arxiv = "https://arxiv.org"
sections = soup.find_all('dl')


class Result:
  title = ""
  authors = ""
  url = ""
  abstract = ""



new = sections[0]
links = new.find_all('dt')
entries = new.find_all('dd')

search_keywords = []
search_authors = []
search_all = []
keywords = [
    'hydrodynamic',
    'hydrodynamics',
    '"effective field theory"',
    '"kinetic theory"',
    '"active matter"',
    'active'
]

authors = [
    "Rahul Nandkishore",
    "Andrew Lucas",
    "Thomas Scaffidi",
    "Paolo Glorioso",
    "Sean Hartnoll",
    ]


for i, entry in enumerate(entries):

    result = Result()
    title = entry.find_all("div", {"class": "list-title"})[0]
    for span in title.find_all("span"):
        span.extract()
    title = title.text.strip()

    link = links[i].find_all("span", {"class": "list-identifier"})[0]
    link = link.find_all('a', href=True, title = True)[0]["href"].strip()
    link = arxiv + link

    abstract = entry.find_all("p")[0].text.strip()

    auths = entry.find_all("div", {"class":"list-authors"})[0].find_all("a")
    auths = [author.text for author in auths]

    
    result.title = title
    result.abstract = abstract
    result.url = link
    result.authors = auths
  

    # check keywords
    for keyword in keywords:
        if keyword in result.title or keyword in result.abstract:
            search_keywords.append(result)
    
    # check authors
    for author in authors:
        if author in result.authors:
            search_authors.append(result)
    
    if (result not in search_authors) and (result not in search_keywords):
        search_all.append(result)




# create a html file to which to put the results
with open("index.html", "w", encoding="utf-8") as f:

    # add the header, which is stored in a different file
    with open("head.html","r") as g:
            for line in g.readlines():
                f.write(line)
    f.write("<body>\n")
    try:
        f.write("<h2>Authors:</h2>\n")
        for result in search_authors:
            
            print(result.title)
            print(result.authors)


            f.write("<h3>{}</h3>\n".format(result.title))
            f.write("<a href = \"{}\" target = \"_blank\">{}</a>\n<br>\n".format(result.url, result.url))
            f.write("<br>\n")

            authors_ = ""
            for author in result.authors:
                authors_ = authors_ + ", " + author
                if authors_[0] == ",":
                    authors_ = authors_[2:]

            f.write("<i>{}</i>\n".format(authors_))
            f.write("<br>\n")

            f.write("{}\n".format(result.abstract))
            f.write("<br>\n")
            f.write("<br>\n")
    except: pass
    try:
        f.write("<h2>Keywords:</h2>\n")
        for result in search_keywords:
            
            print(result.title)
            print(result.authors)


            f.write("<h3>{}</h3>\n".format(result.title))
            f.write("<a href = \"{}\" target = \"_blank\">{}</a>\n<br>\n".format(result.url, result.url))
            f.write("<br>\n")
            authors_ = ""
            for author in result.authors:
                authors_ = authors_ + ", " + author
                if authors_[0] == ",":
                    authors_ = authors_[2:]

            f.write("<i>{}</i>\n".format(authors_))
            f.write("<br>\n")

            f.write("{}\n".format(result.abstract))
            f.write("<br>\n")
            f.write("<br>\n")
    except: pass
    try:
        f.write("<h2>All Papers:</h2>\n")
        for result in search_all:
            
            print(result.title)
            print(result.authors)


            f.write("<h3>{}</h3>\n".format(result.title))
            f.write("<a href = \"{}\" target = \"_blank\">{}</a>\n<br>\n".format(result.url, result.url))
            f.write("<br>\n")
            authors_ = ""
            for author in result.authors:
                authors_ = authors_ + ", " + author
                if authors_[0] == ",":
                    authors_ = authors_[2:]

            f.write("<i>{}</i>\n".format(authors_))
            f.write("<br>\n")

            f.write("{}\n".format(result.abstract))
            f.write("<br>\n")
            f.write("<br>\n")
    except: pass
 

    f.write("</body>")