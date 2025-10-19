import feedparser
from datetime import datetime

# RSS feed URLs
FEEDS = {
    "NASA": "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "Space.com": "https://www.space.com/feeds/all",
    "Spaceflight Now": "https://spaceflightnow.com/feed/"
}

def fetch_headlines(limit=20):
    """Fetch headlines from all RSS feeds"""
    all_headlines = []
    
    for source_name, feed_url in FEEDS.items():
        try:
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries[:limit]:
                headline = {
                    "title": entry.get("title", "No title"),
                    "summary": entry.get("summary", "No summary"),
                    "url": entry.get("link", ""),
                    "source": source_name,
                    "published_at": entry.get("published", "Unknown")
                }
                all_headlines.append(headline)
        except Exception as e:
            print(f"Error fetching {source_name}: {e}")
            continue
    
    return all_headlines
