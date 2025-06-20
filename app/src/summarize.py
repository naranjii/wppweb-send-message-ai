from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if len(text) > 1024:
        text = text[:1024]
    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]["summary_text"]
