import os

from urllib.request import urlretrieve
import openai

import datetime
import json

from openai import generate_dalle_image
from openai import caption_image_fron_url

def get_filename():
    return datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")

description = """ a simple image of a skyscraper in the style of a city building game. 
the skyscraper should be isolated and surrounded by a simple 2 lanes road, 
and it should be represented be in the angle of a 2D city building game but with 3D like buildings. 
The viewpoint should be the usual one in 2D city building games and the skyscraper should be in the centre of the image. """

if os.path.exists('metadata.json'):
    meta = json.load(open('metadata.json', 'rb'))
else:
    meta = {}

print("Found " + str(len(meta)) + " files in metadata.json")

for i in range(14):

    try:
        x = generate_dalle_image(description)

        caption = caption_image(x[0].url)

        print(x[0].url)
        print()
        print(caption)
        print()

        img_filename = os.path.join('data', get_filename() + '.png')

        urlretrieve(x[0].url, img_filename)

        meta.update({img_filename: caption})

    except Exception as e: 
        print(e)
        print("Something went wrong with the API, saving the metadata.")
        break

json.dump(meta, open('metadata.json', 'w'), indent=4)