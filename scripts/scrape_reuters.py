import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from collections import Counter

url = "https://www.reuters.com/technology/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/"
}

print("Fetching Reuters Technology page...")
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Error: Failed with status {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, "html.parser")
news_data = []
list_of_articles = soup.find_all("li", {"class": "story-collection__list-item__j4SQe"})
if not list_of_articles:
    print("No articles found—check HTML!")
    exit()

# Normalize function
def normalize_title(title):
    title = title.lower()
    title = title.replace("artificial intelligence", "ai").replace("technology—" , "tech").replace("technology ", "tech")
    return title

# Main headline
headline_content = list_of_articles[0]
headline = headline_content.get_text(strip=True, separator='@').split('@')[0]
headline_normalized = normalize_title(headline)
link = headline_content.find('a')['href']
if not link.startswith("http"):
    link = "https://www.reuters.com" + link
news_data.append({
    "title": headline,
    "link": link,
    "source": "Reuters",
    "date": datetime.now().strftime("%Y-%m-%d")
})
print(f"Main Article: {headline}")

# Other articles
for i, each_article in enumerate(list_of_articles[1:10], 1):
    content = each_article.get_text(strip=True, separator='@').split('category', 1)[1].split('@')[1]
    content_normalized = normalize_title(content)
    link = each_article.find("a")['href']
    if not link.startswith("http"):
        link = "https://www.reuters.com" + link
    news_data.append({
        "title": content,
        "link": link,
        "source": "Reuters",
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    print(f"Article {i}: {content}")

# Keyword count with normalized titles
keywords = ["ai", "tech", "robotics", "quantum", "startup"]
word_counts = Counter(" ".join([normalize_title(item["title"]) for item in news_data]).split())
top_keywords = {kw: word_counts[kw] for kw in keywords if kw in word_counts}

file_path = "../data/reuters_news.csv"
df = pd.DataFrame(news_data)
try:
    existing_df = pd.read_csv(file_path)
    df = pd.concat([existing_df, df]).drop_duplicates(subset=["title"])
    print(f"Appended {len(news_data)} new articles to existing CSV")
except FileNotFoundError:
    print("No existing CSV—creating new one")
df.to_csv(file_path, index=False)
print(f"\nSaved/Updated {len(df)} total articles to {file_path}")
print(f"Top keywords: {top_keywords}")