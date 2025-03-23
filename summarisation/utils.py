from transformers import pipeline
from gtts import gTTS
from IPython.display import Audio, display

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    Returns 'POSITIVE' or 'NEGATIVE'.
    """
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    return result['label']

def summarize_text(text):
    """
    Summarize the given text.
    Returns a summarized version of the text.
    """
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def text_to_speech_hindi(text, filename="output.mp3"):
    """
    Convert the given text to Hindi speech and save it as an MP3 file.
    Returns the filename of the saved audio.
    """
    tts = gTTS(text=text, lang='hi')
    tts.save(filename)
    return filename

def play_audio(filename):
    """
    Play the audio file using IPython's Audio display.
    """
    display(Audio(filename))