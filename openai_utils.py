import os
import openai

api_key = os.getenv('OPENAI_API_KEY')
assert api_key is not None, "You have to set an environment variable OPENAI_API_KEY with your OpenAI API key"
openai.api_key = api_key

txt_model = "gpt-3.5-turbo"

def generate_dalle_image(prompt, size, img_model):
    
    return openai.images.generate(
        model=img_model,
        prompt=prompt,
        size=size,
        quality="standard",
        n=1,
    ).data[0].url


def caption_image_from_url(url):

    return openai.chat.completions.create(
        model=txt_model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Write a synthetic description for the following image."},
                        {
                            "type": "image_url",
                            "image_url": {
                            "url": url,
                        },
                    },
                ],
            }
        ],
        max_tokens=50,
    ).choices[0].message.content