# saving.py 
# functions to save articles in different formats

def save_as_html(articles, output_file="results.html"):
    """Save the filtered articles as an HTML file."""
    with open(output_file, "w") as f:
        f.write("<html><head><title>Filtered Articles</title></head><body>")
        f.write("<h1>Filtered Articles</h1>")
        for article in articles:
            f.write(f"<h2><a href='{article['link']}' target='_blank'>{article['title']}</a></h2>")
            f.write(f"<p><strong>Authors:</strong> {', '.join(article['authors'])}</p>")
            f.write(f"<p>{article['description']}</p>")
            f.write("<hr>")
        f.write("</body></html>")