def filter(articles, keywords=None, authors=None):
    """Filter articles by keywords or author names."""
    filtered = []
    for article in articles:
        # Check keywords
        if keywords:
            if any(keyword.lower() in article['description'].lower() for keyword in keywords):
                filtered.append(article)
                continue

        # Check authors
        if authors:
            if any(author.lower() in ', '.join(article['authors']).lower() for author in authors):
                filtered.append(article)
                continue

    return filtered

