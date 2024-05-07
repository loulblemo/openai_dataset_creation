import os

import random
import datetime
import json

from urllib.request import urlretrieve

from openai_utils import generate_dalle_image
from openai_utils import caption_image_fron_url

def generate_filename():
    return datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S_" + str(random.randint(0, 1000)))

description = """ a simple image of a skyscraper in the style of a city building game. 
the skyscraper should be isolated and surrounded by a simple 2 lanes road, 
and it should be represented be in the angle of a 2D city building game but with 3D like buildings. 
The viewpoint should be the usual one in 2D city building games and the skyscraper should be in the centre of the image. """

if os.path.exists('metadata.json'):
    meta = json.load(open('metadata.json', 'rb'))
else:
    meta = {}

print("Found " + str(len(meta)) + " files in metadata.json")


def generate_dataset(prompt, num_datapoints):

    for i in range(num_datapoints):

        try:
            image_url = generate_dalle_image(description)
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

    prompt = description

    generate_dataset(prompt, num_datapoints=50)