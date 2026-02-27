from openai import OpenAI

client = OpenAI(api_key=" ")


# modules/stt_module.py

# modules/stt_module.py

def speech_to_text(audio_bytes, use_mock=False):
    """
    Convert audio to text. 
    If use_mock=True, return a placeholder text for demo.
    """
    if use_mock:
        # Return a mock answer for demo purposes
        return "This is a mock answer for demo purposes."
    
    # Real speech-to-text functionality can be added here if needed
    # For demo/offline mode, we simply return a placeholder
    return "Speech-to-text not implemented (mock mode off)."
