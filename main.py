import feedparser
from colorama import Fore, Style

# Define the feed URLs
urls = [
    'https://feeds.feedburner.com/TroyHunt',
    'https://threatpost.com/feed',
    'https://www.darkreading.com/rss_simple.asp',
    'https://www.zdnet.com/news/rss.xml',
    'https://www.schneier.com/blog/atom.xml',
    'https://www.csoonline.com/index.rss',
    'https://www.securityweek.com/rss',
    'https://krebsonsecurity.com/feed/',
    'https://thehackernews.com/feeds/posts/default?alt=rss'
]

# Define the maximum number of articles to show
MAX_ARTICLES = 5

# Define colors for the output
TITLE_COLOR = Fore.CYAN
LINK_COLOR = Fore.YELLOW
RESET_COLOR = Style.RESET_ALL

for url in urls:
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Print the feed title
    print(f'{TITLE_COLOR}{feed.feed.title}:{RESET_COLOR}')

    # Loop through the feed entries and print the titles and links
    for i, entry in enumerate(feed.entries[:MAX_ARTICLES]):
        # Get the title and link
        title = entry.title
        link = entry.link

        # Print the title and link
        print(f'{TITLE_COLOR}{i+1}. {title}{RESET_COLOR}')
        print(f'{LINK_COLOR}   {link}{RESET_COLOR}')

    # Add a blank line between feeds
    print()
