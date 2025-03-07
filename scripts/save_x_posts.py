import pandas as pd
from datetime import datetime
from collections import Counter

# X posts from me
x_posts = [
    {"text": "AI is killing it in 2025 #AI", "username": "@TechVibe", "date": "2025-03-07"},
    {"text": "Just tested an AI chatbot—wow #AI", "username": "@DigitalNomad", "date": "2025-03-06"},
    {"text": "AI ethics debate heating up #AI", "username": "@ThinkerX", "date": "2025-03-07"},
    {"text": "New AI framework dropped today #AI", "username": "@CodeNinja", "date": "2025-03-07"},
    {"text": "AI in education is next big thing #AI", "username": "@EduTechie", "date": "2025-03-06"},
    {"text": "Building an AI app this week #AI", "username": "@DevDiary", "date": "2025-03-07"},
    {"text": "AI funding hits record high #AI", "username": "@StartupBuzz", "date": "2025-03-06"},
    {"text": "AI robots at work—crazy! #AI", "username": "@FutureWorks", "date": "2025-03-07"},
    {"text": "AI’s job impact is real #AI", "username": "@EconBit", "date": "2025-03-06"},
    {"text": "AI art tools are unreal #AI", "username": "@ArtBot", "date": "2025-03-07"}
]

# Keyword counts
all_texts = [post["text"].lower() for post in x_posts]
keywords = ["ai", "chatbot", "robot", "funding", "ethics"]
word_counts = Counter(" ".join(all_texts).split())
top_keywords = {kw: word_counts[kw] for kw in keywords if kw in word_counts}

# Save to CSV
df = pd.DataFrame(x_posts)
df.to_csv("../data/x_posts.csv", index=False)  # Same path as BBC
print(f"Saved {len(x_posts)} X posts to ../data/x_posts.csv")
print(f"Top keywords: {top_keywords}")