import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"


response = requests.get(URL)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')


headlines = soup.find_all(['h1', 'h2', 'h3','h4', 'title'])


with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        text = headline.get_text(strip=True)
        if text:
            file.write(text + "\n")

print(" Parsed Data has been saved to headlines.txt")
