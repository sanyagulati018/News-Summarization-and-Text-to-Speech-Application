import requests
from transformers import pipeline
from gtts import gTTS
from IPython.display import Audio, display
import pandas as pd

def fetch_news(company_name, api_key):
    url = f"https://gnews.io/api/v4/search?q={company_name}&lang=en&country=us&max=10&token={api_key}"
    response = requests.get(url)
    data = response.json()
    print("API Response:", data)
    articles = []
    if 'articles' in data:  # Check if 'articles' key exists
        for item in data['articles']:
            articles.append({
                "title": item['title'],
                "link": item['url'],
                "summary": item['description'],
                "content": item['content']
            })
    else:
        print("Error: 'articles' key not found in API response.")
        if 'message' in data:
            print(f"API Error: {data['message']}")

    return articles
def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    return result['label']
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
def text_to_speech_hindi(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='hi')
    tts.save(filename)
    return filename
def main(company_name, api_key):
    # Step 1: Fetch News Articles
    articles = fetch_news(company_name, api_key)

    # Step 2: Analyze Sentiment, Summarize, and Generate TTS
    results = []
    for i, article in enumerate(articles):
        print(f"Processing Article {i+1}: {article['title']}")

        # Analyze Sentiment
        sentiment = analyze_sentiment(article['content'])

        # Summarize the Article
        summary = summarize_text(article['content'])

        # Generate Hindi TTS Audio
        tts_file = text_to_speech_hindi(summary, filename=f"output_{i+1}.mp3")

        # Append Results
        results.append({
            "title": article['title'],
            "summary": summary,
            "sentiment": sentiment,
            "audio_file": tts_file
        })

        # Display Results
        print(f"Title: {article['title']}")
        print(f"Summary: {summary}")
        print(f"Sentiment: {sentiment}")
        print(f"Audio File: {tts_file}")

        # Play the Hindi TTS Audio
        print("Playing Hindi TTS audio...")
        display(Audio(tts_file))
        print("\n")

    return results
# Input: Company Name and API Key
company_name = "google"
api_key = "dc4fd873f3ed8116059deb4eebeb8f84"  # Replace with your GNews API key

results = main(company_name, api_key)