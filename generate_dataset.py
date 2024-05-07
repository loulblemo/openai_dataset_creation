import os

import random
import datetime
import json

from urllib.request import urlretrieve

from openai_utils import generate_dalle_image
from openai_utils import caption_image_from_url

def generate_filename():
    return datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S_" + str(random.randint(0, 1000)) + '.png')

description = """  """

print("Found " + str(len(meta)) + " files in metadata.json")


def generate_dataset(prompt, dataset_folder, num_datapoints, img_size, img_model):

    meta = {}

    for i in range(num_datapoints):

        try:
            image_url = generate_dalle_image(prompt=prompt, size=img_size, img_model=img_model)
            caption = caption_image_from_url(image_url)
            img_filename = os.path.join(dataset_folder, 'data', generate_filename())

            urlretrieve(image_url, img_filename)

            meta.update({img_filename: caption})

        except Exception as e: 
            print("Something went wrong with the API, saving the metadata. See ERROR:")
            print(e)
            break

json.dump(meta, open('metadata.json', 'w'), indent=4)


if __name__ == "__main__":

    prompt_file = "example_prompt.txt"
    dataset_folder = "skyscrapers"

    os.makedirs(dataset_folder, exist_ok=True)
    os.makedirs(os.path.join(dataset_folder, 'data'), exist_ok=True)

    with open(prompt_file, "r") as txt_file:
        prompt = txt_file.read()

    prompt = description

    generate_dataset(prompt, 
                     dataset_folder=dataset_folder,
                     num_datapoints=10, 
                     img_size="256x256", 
                     img_model='dall-e-2'
                     )