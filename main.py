from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="alloy",
  input="Hola soy Juan y bienvenido a un nuevo video!"
)

response.stream_to_file(speech_file_path)