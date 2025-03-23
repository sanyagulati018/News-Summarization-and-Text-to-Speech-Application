from api import fetch_news
from utils import analyze_sentiment, summarize_text, text_to_speech_hindi, play_audio

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
        play_audio(tts_file)
        print("\n")

    return results

# Input: Company Name and API Key
if __name__ == "__main__":
    company_name = "google"
    api_key = "dc4fd873f3ed8116059deb4eebeb8f84"  # Replace with your GNews API key
    results = main(company_name, api_key)