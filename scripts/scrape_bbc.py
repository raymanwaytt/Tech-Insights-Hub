import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from collections import Counter

# URL and headers
url = "https://www.bbc.com/news/technology"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# Fetch page
print("Fetching BBC Technology page...")
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Error: Failed with status {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, "html.parser")
articles = soup.find_all("h2", {"data-testid": "card-headline"})
if not articles:
    print("No articles found—check HTML!")
    exit()

news_data = []
all_titles = []

# Process articles
for i, article in enumerate(articles[:10], 1):
    title = article.get_text(strip=True)
    all_titles.append(title.lower())
    link = article.find_parent("a")["href"] if article.find_parent("a") else "No link"
    if not link.startswith("http"):
        link = "https://www.bbc.com" + link
    news_data.append({
        "title": title,
        "link": link,
        "source": "BBC",
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    print(f"Article {i}: {title}")

# Keyword counts
keywords = ["ai", "tech", "robotics", "quantum", "startup"]
word_counts = Counter(" ".join(all_titles).split())
top_keywords = {kw: word_counts[kw] for kw in keywords if kw in word_counts}

# Save to CSV
df = pd.DataFrame(news_data)
df.to_csv("../data/bbc_news.csv", index=False)
print(f"\nSaved {len(news_data)} articles to ../data/bbc_news.csv")
print(f"Top keywords: {top_keywords}")