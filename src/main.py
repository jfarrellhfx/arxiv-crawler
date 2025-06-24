# main.py
# Entry point for the arXiv crawler.

import json
from fetcher import fetch_rss_feed
from saving import save_as_html
from filters import filter

def main():
    # Load configuration
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # Fetch articles
    articles = fetch_rss_feed(config.get('url'))
    
    # filter articles
    filtered_articles = filter(
        articles,
        keywords=config.get('keywords'),
        authors=config.get('authors')
    )

    # Save articles as HTML
    save_as_html(filtered_articles, config.get('output_file', 'results.html'))

if __name__ == "__main__":
    main()
