import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    paragraphs = soup.find_all("p")
    text = "\n".join(p.text for p in paragraphs if len(p.text) > 50)
    return text.strip()
