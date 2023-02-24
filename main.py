#!/usr/bin/python3

import re
import feedparser
import argparse
import logging
from colorama import Fore, Style

# Define the feed URLs
urls = [
    'https://feeds.feedburner.com/TroyHunt',
    'https://threatpost.com/feed',
    'https://www.zdnet.com/news/rss.xml',
    'https://www.schneier.com/blog/atom.xml',
    'https://www.csoonline.com/index.rss',
    'https://www.securityweek.com/rss',
    'https://krebsonsecurity.com/feed',
    'https://www.darkreading.com/rss.xml',
    'https://feeds.feedburner.com/TheHackersNews',
    'https://nakedsecurity.sophos.com/feed',
    'https://www.bleepingcomputer.com/feed/'
]

# Define colors for the output
TITLE_COLOR = Fore.CYAN
LINK_COLOR = Fore.YELLOW
RESET_COLOR = Style.RESET_ALL

def main():
    # Configure argument parser
    parser = argparse.ArgumentParser(description='Display recent articles from security news feeds.')
    parser.add_argument('-n', '--num-articles', type=int, default=5, help='Number of articles to display (default: 5)')
    parser.add_argument('-f', '--output-format', choices=['text', 'html', 'json'], default='text', help='Output format (default: text)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    parser.add_argument('-k', '--keyword', nargs='+', help='Keywords to search for in article titles')
    args = parser.parse_args()

    # Configure logging
    if args.verbose:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    # Parse the RSS feeds
    articles = []
    for url in urls:
        feed = feedparser.parse(url)
        if feed.bozo:
            logging.warning(f'Unable to parse feed: {url}')
            continue
        for entry in feed.entries:
            if 'title' not in entry or 'link' not in entry:
                logging.warning(f'Missing title or link in entry: {entry}')
                continue
            articles.append(entry)

    # Sort the articles by date
    articles.sort(key=lambda x: x.published_parsed, reverse=True)

    # Filter the articles by keyword, if specified
    keywords = args.keyword
    if keywords:
        if isinstance(keywords, list):
            keywords = ','.join(keywords)
        keywords = keywords.lower().split(',')
        articles = [a for a in articles if any(kw in a.title.lower() for kw in keywords)]


    # Limit the number of articles to display
    articles = articles[:args.num_articles]

    # Output the articles in the specified format
    if args.output_format == 'text':
        for i, article in enumerate(articles):
            print(f'{TITLE_COLOR}{i+1}. {article.title}{RESET_COLOR}')
            print(f'{LINK_COLOR}   {article.link}{RESET_COLOR}')
            print()
    elif args.output_format == 'html':
        print('<ul>')
        for article in articles:
            print(f'<li><a href="{article.link}">{article.title}</a></li>')
        print('</ul>')
    elif args.output_format == 'json':
        import json
        print(json.dumps([{'title': a.title, 'link': a.link} for a in articles], indent=4))

if __name__ == '__main__':
    main()