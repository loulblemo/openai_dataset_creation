import os

import json

from urllib.request import urlretrieve

from openai_utils import generate_dalle_image
from openai_utils import caption_image_from_url

from utils import generate_filename
from utils import write_json_as_csv
from utils import load_from_csv
# description = """  """
# print("Found " + str(len(meta)) + " files in metadata.json")


def generate_dataset(prompt, dataset_folder, meta, num_datapoints, img_size, img_model):

    if meta is None:
        meta = {}

    for i in range(num_datapoints):

        try:

            # image_url = generate_dalle_image(prompt=prompt, size=img_size, img_model=img_model)
            # caption = caption_image_from_url(image_url)
            # img_filename = os.path.join(dataset_folder, 'data', generate_filename())
            # urlretrieve(image_url, img_filename)
            # meta.update({img_filename: caption})

            meta.update({generate_filename() : 'test' + str(i)})

        except Exception as e: 
            print("Something went wrong with the API, saving the metadata. See ERROR:")
            print(e)
            break

    return meta


if __name__ == "__main__":

    prompt_file = "example_prompt.txt"
    dataset_folder = "skyscrapers"
    
    os.makedirs(dataset_folder, exist_ok=True)
    os.makedirs(os.path.join(dataset_folder, 'data'), exist_ok=True)

    with open(prompt_file, "r") as txt_file:
        prompt = txt_file.read()

    metadata_csv_file = os.path.join(dataset_folder, 'metadata.csv')

    if os.path.exists(metadata_csv_file):
        print("Metadata found, updating the current meta with new files")
        meta = load_from_csv(metadata_csv_file)
    else: meta = None

    meta = generate_dataset(prompt, 
                            dataset_folder=dataset_folder,
                            meta=meta,
                            num_datapoints=10, 
                            img_size="256x256", 
                            img_model='dall-e-2'
                            )

    print("Done creating dataset. Dataset size is currently " + str(len(meta)) + str(" files"))

    write_json_as_csv(meta, metadata_csv_file)