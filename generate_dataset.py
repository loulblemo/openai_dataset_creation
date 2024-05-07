import os

import random
import datetime
import json

from urllib.request import urlretrieve

from openai_utils import generate_dalle_image
from openai_utils import caption_image_fron_url

def generate_filename():
    return datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S_" + str(random.randint(0, 1000)))

description = """  """

if os.path.exists('metadata.json'):
    meta = json.load(open('metadata.json', 'rb'))
else:
    meta = {}

print("Found " + str(len(meta)) + " files in metadata.json")


def generate_dataset(prompt, num_datapoints, img_size, img_model):

    for i in range(num_datapoints):

        try:
            image_url = generate_dalle_image(prompt, size=img_size)
            caption = caption_image(image_url)

            print(image_url)
            print()
            print(caption)
            print()

            img_filename = os.path.join('data', generate_filename() + '.png')

            urlretrieve(image_url, img_filename)

            meta.update({img_filename: caption})

        except Exception as e: 
            print(e)
            print("Something went wrong with the API, saving the metadata.")
            break

json.dump(meta, open('metadata.json', 'w'), indent=4)

if __name__ == "__main__":

    prompt_file = "example_prompt.txt"

    with open(prompt_file, "r") as txt_file:
        prompt = txt_file.read()

    prompt = description

    generate_dataset(prompt, num_datapoints=50, img_size="1024x1024", img_model='dall-e-2')