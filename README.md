# Tech Innovations Insights Hub

Welcome to the **Tech Innovations Insights Hub**—a daily scrape-and-analyze project tracking the pulse of tech in 2025. This repo pulls tech news and social buzz from BBC, Reuters, and X, stores it in CSVs, and sets the stage for trend-spotting. Think of it as a live portfolio flex—scraping, data wrangling, and (soon) visuals, all in one.

## What’s This About?

- **Sources**:
  - **BBC**: Broad tech news from `https://www.bbc.com/innovation/technology`.
  - **Reuters**: Deep tech dives from `https://www.reuters.com/technology/`.
  - **X**: Real-time #AI chatter from `https://x.com/search?q=%23AI&f=live`.
- **Output**: 
  - Daily CSVs in `data/`—raw articles and posts.
  - Keywords tracked: `ai`, `tech`, `robotics`, `quantum`, `startup`...
- **Goal**:
    The end goal is to scrape daily tech updates from BBC, Reuters, and X (#AI) into a dataset that tracks emerging trends via keyword analysis. This builds a dynamic showcase of real-time data collection and insights, ready for visualization.

## Structure
- **`data/`**:
  - `bbc_news.csv`: 17 articles (Day 3).
  - `reuters_news.csv`: Total of 10 articles (Day 3).
  - `x_posts.csv`: 10 placeholder #AI posts.
- **`scripts/`**:
  - `scrape_bbc.py`: BBC scraper—titles, links, dates.
  - `scrape_reuters.py`: Reuters scraper—handles main + list articles.
  - `scrape_x_posts.py`: X scraper—Selenium, #AI focus .

## How It Works
1. **Scrape**: Daily runs grab articles (BBC, Reuters) and #AI posts (X).
2. **Store**: Append to CSVs—`title/text`, `link`, `source/username`, `date`.
3. **Analyze**: Count keywords—e.g., Day 3: BBC (`tech: 1, quantum: 1`), Reuters (`ai: 3`).

## Tools
- **Python**: `requests`, `BeautifulSoup`, `selenium`, `webdriver-manager`, `pandas`.