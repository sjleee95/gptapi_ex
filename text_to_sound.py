from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#os.environ.get 부분을 변수에 넣지 않고 gpt_api_key 부분에 그냥 넣어도 됨.
OPEN_API_KEY = os.environ.get("OPEN_API_KEY")

gpt_api_key = OPEN_API_KEY

client = OpenAI(
    # api_key="gpt api key 넣기"
    api_key=gpt_api_key
)
#print("인증성공")

#Send question to GPT Model
from pathlib import Path
with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice="alloy",
    input="안녕하세요."
) as response:
    response.stream_to_file("speech.mp3")

