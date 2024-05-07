import os
import json

import argparse

from urllib.request import urlretrieve

from openai_utils import generate_dalle_image
from openai_utils import caption_image_from_url

from utils import generate_filename
from utils import write_json_as_csv
from utils import load_from_csv


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

    parser = argparse.ArgumentParser(description="Generate a diffusion dataset using OpenAI API")
    
    parser.add_argument('--prompt-file', '-p', 
                        dest='prompt_file', 
                        type=str, 
                        default='example_prompt.txt',
                        help="Text file containing the text prompt for image generation")
    parser.add_argument('--output-folder', 
                        '-o', 
                        dest='output_folder', 
                        type=str, 
                        default='my_dataset',
                        help="Output folder where to save the dataset")
    parser.add_argument('--size', 
                        '-s', 
                        dest='img_size', 
                        type=str, 
                        default='512x512',
                        help="The size of output images in pixels, note that some models only accept particular resolutions")
    parser.add_argument('--num-datapoints', 
                        '-n', 
                        dest='num_datapoints', 
                        type=int, 
                        default=10,
                        help="How many datapoints to generate")
    parser.add_argument('--model', 
                        '-m', 
                        dest='model', 
                        type=str, 
                        default='dall-e-2',
                        help="The image model to be used, default is dall-e-2 as it is cheaper")

    args = parser.parse_args()

    os.makedirs(args.output_folder, exist_ok=True)
    os.makedirs(os.path.join(args.output_folder, 'data'), exist_ok=True)

    with open(args.prompt_file, "r") as txt_file:
        prompt = txt_file.read()

    metadata_csv_file = os.path.join(args.output_folder, 'metadata.csv')

    if os.path.exists(metadata_csv_file):
        print("Metadata found, updating the current meta with new files")
        meta = load_from_csv(metadata_csv_file)
    else: meta = None

    meta = generate_dataset(prompt, 
                            dataset_folder=args.output_folder,
                            meta=meta,
                            num_datapoints=args.num_datapoints, 
                            img_size=args.img_size, 
                            img_model=parser.model
                            )

    print("Done creating dataset. Dataset size is currently " + str(len(meta)) + str(" files"))

    write_json_as_csv(meta, metadata_csv_file)