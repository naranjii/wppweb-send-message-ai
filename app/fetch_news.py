import requests
from bs4 import BeautifulSoup

def get_top_news_links(limit=5):
    url = "https://www.nytimes.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    articles = soup.find_all("a", href=True)
    seen = set()
    links = []

    for a in articles:
        href = a["href"]
        if href.startswith("/"):
            href = "https://www.nytimes.com" + href
        if "/202" in href and href not in seen:
            seen.add(href)
            links.append(href)
        if len(links) >= limit:
            break
    return links
