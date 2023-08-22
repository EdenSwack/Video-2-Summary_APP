# pip install moviepy
import requests
from moviepy.editor import *
import uuid

# API endpoints and keys
A2T_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
SUM_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
TRANSLATE = "https://api.cognitive.microsofttranslator.com/"

HF_KEY = {"Authorization": "Your HuggingFace API key here"}
MSFT_KEY = "Your API key for microsoft endpoint here"


# Function that translates audio to text
def aud2text(filename):
    with open(filename, "rb") as f:
        data = f.read()

    response = requests.post(A2T_URL, headers=HF_KEY, data=data)
    return response.json()


# Function that summarizes text
def Summarize(payload):
    response = requests.post(SUM_URL, headers=HF_KEY, json=payload)
    return response.json()


# Function that call main function that uses other funcs to turn an uploaded
# video into a text summary
def Vid2Sum(vid_file):
    video = VideoFileClip(vid_file)
    audio_file = "C:\\temp2\\converted_audio.mp3"
    video.audio.write_audiofile(audio_file)

    text = aud2text(audio_file)
    sum_text = Summarize(text["text"])
    return sum_text[0]["summary_text"]


# Tranlates text to desired output text by user
def translate(text, input_lang, output_lang):
    params = {
        "api-version": "3.0",
        "from": input_lang,
        "to": get_language_code(output_lang),
    }

    url = f"{TRANSLATE}/translate"

    headers = {
        "Ocp-Apim-Subscription-Key": MSFT_KEY,
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Region": "Global",
        "X-ClientTraceId": str(uuid.uuid4()),
    }
    body = [{"text": text}]

    response = requests.post(url, params=params, headers=headers, json=body)

    if response.status_code == 200:
        translation = response.json()[0]["translations"][0]["text"]
        return translation
    else:
        print(f"Translation failed. Status Code: {response.status_code}")
        print(response.content.decode())
        return None


# Gets the correct abbreaviation of languafe selection
def get_language_code(language):
    language_mapping = {
        "english": "en",
        "spanish": "es",
        "french": "fr",
        "german": "de",
        "italian": "it",
        "portuguese": "pt",
        "chinese": "zh-Hans",
        "japanese": "ja",
        "russian": "ru",
        "arabic": "ar",
        "hindi": "hi",
        "hebrew": "he",
    }

    return language_mapping.get(language.lower(), None)
