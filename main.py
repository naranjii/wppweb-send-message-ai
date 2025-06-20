from app.fetch_news import get_top_news_links
from app.parse_article import extract_article_text
from app.summarize import summarize_text
from app.send_whatsapp import send_whatsapp_message

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
    print("[+] Enviando via WhatsApp...")
    send_whatsapp_message(full_message)

if __name__ == "__main__":
    main()
