import requests
from bs4 import BeautifulSoup

page = requests.get("https://arxiv.org/list/cond-mat/new")
soup = BeautifulSoup(page.content, 'html.parser')
arxiv = "https://arxiv.org"
sections = soup.find_all('dl')

def write_entries(file, collection):
    f = file
    try: 
        for result in collection:
            f.write("<h3>{}</h3>\n".format(result.title))
            f.write("<a href = \"{}\" target = \"_blank\">{}</a>\n<br>\n".format(result.url, result.url))

            authors_ = ""
            for author in result.authors:
                authors_ = authors_ + ", " + author
                if authors_[0] == ",":
                    authors_ = authors_[2:]
            f.write("<i>{}</i>\n".format(authors_))
            
            f.write("<p>")
            f.write("{}\n".format(result.abstract))
            f.write("</p>")
            f.write("<br>\n")
            f.write("<br>\n")
    except:
        pass

class Result:
  def __init__(self) -> None:
        self.title = ""
        self.authors = ""
        self.url = ""
        self.abstract = ""
        pass
   
 
  



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
with open("index.html", "a", encoding="utf-8") as f:

    # add the header, which is stored in a different file
    with open("head.html","r") as g:
            for line in g.readlines():
                f.write(line)
    f.write("<h2 style = \"margin-top:10px\">Authors:</h2>\n")
    f.write("<hr color = \"#bbb\" style = \"margin-bottom:20px\">\n")
    write_entries(f,search_authors)

       
    
    f.write("<h2 style = \"margin-top:10px\">Keywords:</h2>\n")
    f.write("<hr color = \"#bbb\" style = \"margin-bottom:20px\">\n")
    write_entries(f,search_keywords)
        
 
    f.write("<h2 style = \"margin-top:10px\">All Papers</h2>\n")
    f.write("<hr color = \"#bbb\" style = \"margin-bottom:20px\">\n")
    write_entries(f,search_all)

 

    f.write("</body>")