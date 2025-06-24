# arXiv Crawler

This is a simple utility to fetch and filter articles from the RSS feed of the "cond-mat/new" page on arXiv. Users can filter articles by keywords and author names.

## Features
- Fetch articles from the arXiv RSS feed.
- Filter articles by keywords in the title or abstract.
- Filter articles by author names.
- Display filtered results in a user-friendly format.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd arxiv-crawler
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure filters in `config.json`.

## Usage

Run the crawler:
```bash
python src/main.py
```

## License
This project is licensed under the MIT License.
