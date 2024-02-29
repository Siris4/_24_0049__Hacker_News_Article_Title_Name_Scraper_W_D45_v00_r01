from bs4 import BeautifulSoup
import requests

# CONSTANTS:
LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE = 17
title_number = 0

response = requests.get("https://news.ycombinator.com/news")
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# Find the first two article rows by their unique class 'athing'
article_rows = soup.find_all('tr', class_='athing', limit=LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE)

for article_row in article_rows:
    title_number += 1
    # Navigate to the title within each article row
    title_span = article_row.find('span', class_='titleline')
    if title_span:
        title_link = title_span.find('a')
        if title_link:
            title = title_link.text
            print(f"Title {title_number}: {title}")
        else:
            print("Title link not found.")
    else:
        print("Title span not found.")
