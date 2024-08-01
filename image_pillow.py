from PIL import Image

import urllib.request

def display_jpeg_image(url):
    try:
        image_path, _= urllib.request.urlretrieve(url, "test,jpg")
        print(image_path)
        image = Image.open(image_path)
    except Exception as e:
        print("Error:", e)

jpeg_image_path = "https://cdn.kbmaeil.com/news/photo/201904/811074_839900_5653.jpg"
display_jpeg_image(jpeg_image_path)