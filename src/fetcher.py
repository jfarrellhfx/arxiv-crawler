# fetcher.py
# This module provides functions to fetch, filter, and save articles from arXiv.

import feedparser

def fetch_rss_feed(url):
    """Fetch and parse the RSS feed from the given URL."""
    feed = feedparser.parse(url)
    articles = [
        {
            'title': entry.title,
            'description': entry.description,
            'authors': [author.name for author in entry.authors],
            'link': entry.link
        }
        for entry in feed.entries
    ]
    return articles




