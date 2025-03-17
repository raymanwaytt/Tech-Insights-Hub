# Tech Innovations Insights Hub

Welcome to the **Tech Innovations Insights Hub**—a daily scrape-and-analyze project tracking the pulse of tech in 2025. This repo pulls tech news from BBC and Reuters, stores it in CSVs, and sets the stage for trend-spotting. Think of it as a live portfolio flex—scraping, data wrangling, and (soon) visuals, all in one.

## What’s This About?

- **Sources**:
  - **BBC**: Broad tech news from `https://www.bbc.com/innovation/technology`.
  - **Reuters**: Deep tech dives from `https://www.reuters.com/technology/`.
- **Output**: 
  - Daily CSVs in `data/`—raw articles and posts.
  - Keywords tracked: `ai`, `tech`, `robotics`, `quantum`, `startup`...
- **Goal**:
    The end goal is to scrape daily tech updates from BBC and Reuters into a dataset that tracks emerging trends via keyword analysis. This builds a dynamic showcase of real-time data collection and insights, ready for visualization.

## Structure
- **`data/`**:
  - `bbc_news.csv` 
  - `reuters_news.csv`
- **`scripts/`**:
  - `scrape_bbc.py`: BBC scraper—titles, links, dates.
  - `scrape_reuters.py`: Reuters scraper—handles main + list articles.
- **`top_keywords`** : Record of daily keywords count.

## How It Works
1. **Scrape**: Daily runs grab articles (BBC, Reuters).
2. **Store**: Append to CSVs—`title`, `link`, `source`, `date`.
3. **Analyze**: Count keywords—e.g., Day 3: BBC (`tech: 1, quantum: 1`), Reuters (`ai: 3`) & keep daily records.

## Tools
- **Python**: `requests`, `BeautifulSoup`, `pandas`