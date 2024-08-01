from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

OPEN_API_KEY = os.environ.get("OPEN_API_KEY")

gpt_api_key = OPEN_API_KEY

client = OpenAI(
    api_key=gpt_api_key
)

messages = []

while True:
    content = input("사용자:")
    if ('q' == content.lower() or 'ㅂ' == content) : break;
    messages.append({"role":"user","content":content})

    complation = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_response = complation.choices[0].message.content
    print(f"ChatGPT : {chat_response}")
    messages.append({"role":"assistant","content":chat_response})
    
#q를 누르면 대화 종료되게 만들기
