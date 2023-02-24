#!/usr/bin/python3

import os
import sys
import time
import requests
import feedparser
import argparse
import logging
from tqdm import tqdm
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

def main():
    # Define colors for the output
    TITLE_COLOR = Fore.CYAN
    LINK_COLOR = Fore.YELLOW
    RESET_COLOR = Style.RESET_ALL

    # Define the user-agent
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    # Configure argument parser
    parser = argparse.ArgumentParser(description='Display recent articles from security news feeds.')
    parser.add_argument('-n', '--num-articles', type=int, default=5, help='Number of articles to display (default: 5)')
    parser.add_argument('-f', '--output-format', choices=['text', 'html', 'json'], default='text', help='Output format (default: text)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    parser.add_argument('-k', '--keyword', nargs='+', help='Keywords to search for in article titles')
    parser.add_argument('-t', '--timer', type=int, default=0, help='Timer to refresh the articles in minutes (default: 0)')
    args = parser.parse_args()

    # Configure logging
    if args.verbose:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    # Fetch the RSS feeds
    articles = []
    for url in tqdm(urls, desc='Fetching feeds'):
        try:
            response = requests.get(url, headers={'User-Agent': user_agent})
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            if feed.bozo:
                logging.warning(f'Unable to parse feed: {url}')
                continue
            for entry in feed.entries:
                if 'title' not in entry or 'link' not in entry:
                    logging.warning(f'Missing title or link in entry: {entry}')
                    continue
                articles.append(entry)
        except requests.exceptions.RequestException as e:
            logging.warning(f'Unable to fetch feed: {url}, {str(e)}')
            continue

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

    # If timer is specified, wait for the specified time and refresh the articles
    if args.timer:
        logging.info(f"Waiting for {args.timer} minutes...")
        try:
            while True:
                time.sleep(args.timer * 60)                         # convert minutes to seconds
                os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen
                main()                                              # call main function to fetch and display updated articles
        except KeyboardInterrupt:
            logging.info("Timer stopped by user.")
            sys.exit(0)

if __name__ == '__main__':
    main()
