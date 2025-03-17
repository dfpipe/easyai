import requests
from PIL import Image
from io import BytesIO
import os
import base64
from pathlib import Path

class HttpsCall:

    @staticmethod
    def call_with_json_body(url, body):
        headers = {
            "Content-Type": "application/json"  # Important for JSON payloads
        }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error calling {url}: {response.status_code} {response.text}", response)
        return response.json()


def image_to_base64(image: Image.Image) -> str:
    image_io = BytesIO()
    image.save(image_io, format='JPEG')
    return base64.b64encode(image_io.getvalue()).decode('utf-8')

def base64_to_image(base64_str: str) -> Image.Image:
    image_bytes = base64.b64decode(base64_str)
    image_io = BytesIO(image_bytes)
    return Image.open(image_io)

def smart_read_image_v1(image) -> Image.Image:
    # support the following types:
    # 1. base64 (string), 
    # 2. url (string, starts with http), 
    # 3. local file path (string and ends with .jpg, .png, and it exists)
    # 4. PIL Image object
    # 5. Path object
    if isinstance(image, Image.Image):
        return image
    
    if isinstance(image, str):
        if image.startswith('http'):
            response = requests.get(image, timeout=2)
            return Image.open(BytesIO(response.content))

        # the likelihood of the path longer than 4096 is very low
        # this one supports both string or pathlib.Path object
        if len(image) < 4096 and Path(image).exists():
            return Image.open(image)

        try: 
            return base64_to_image(image)
        except Exception as e:
            raise ValueError(f"Assuming the input is base64 encoded image, but failed to read it, longest {image[:100]}") from e
    
    raise ValueError(f"Invalid image: {image}")


