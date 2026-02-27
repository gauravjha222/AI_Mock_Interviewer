
from openai import OpenAI

client = OpenAI(api_key=" ")


def text_to_speech(text):
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )
    return response.read()
