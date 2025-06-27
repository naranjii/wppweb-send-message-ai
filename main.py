from app.src.fetch_news import get_top_news_links
from app.src.parse_article import extract_article_text
from app.src.summarize import summarize_text
from app.src.components.send_whatsapp import send_whatsapp_message
import os

def main():
    print("[+] Coletando links das notícias...")
    links = get_top_news_links(limit=3)

    all_summaries = []
    for url in links:
        print(f"[+] Processando: {url}")
        article_text = extract_article_text(url)
        summary = summarize_text(article_text)
        all_summaries.append(f"{summary}\nFonte: {url}")

    full_message = "\n\n🗞️ *Resumo das Principais Notícias do NYT* 🗞️\n\n" + "\n\n".join(all_summaries)
    with open("data/log.txt", "w", encoding="utf-8") as f:
        f.write(full_message)
    print("[+] Enviando via WhatsApp...")
    send_whatsapp_message(full_message)

if __name__ == "__main__":
    main()
