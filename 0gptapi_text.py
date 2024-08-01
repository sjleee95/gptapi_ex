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
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        #{"role":"system","content": "You are an IT expert."},
        {"role":"user","content":"What is top 5 popular Computer Language in the world?"}
    ]
)

print(response.choices[0].message.content)