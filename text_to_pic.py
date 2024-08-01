import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPEN_API_KEY')

from openai import OpenAI
client = OpenAI(
    api_key=api_key
)

response = client.images.generate(
    model="dall-e-3",
    prompt="Draw me some cute cat wearing boots",
    size="1024x1024",
    quality="standard",
    n=1,
)
image_url=response.data[0].url

print(image_url)
