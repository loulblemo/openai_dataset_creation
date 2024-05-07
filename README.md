# Create a dataset to finetune a text-to-image diffusion model in minutes using Dall-e and ChatGPT from OpenAI

## What is this repo about?

This repo showcases how we can use the OpenAI API to create a dataset that can be used to fine-tune a text-to-image HuggingFace model off the bat.

We will be using Dall-e to generate the Images and ChatGPT to annotate the images with text.

The main script in this repo, generate_dataset.py, creates a dataset folder that can be uploaded to the public HuggingFace Datasets. The output folder will contain a `data` folder with the images, and a `metadata.csv` file, containing the matching between images and text. 

An example of a dataset created using this script can be found here: 
https://huggingface.co/datasets/Loulblemo/diffusion_skyscrapers_city_building

A google colab notebeook demonstrating how to use that dataset to finetune a diffusion model can be found here:
https://github.com/loulblemo/colab_diffusers_finetuning/blob/main/diffusion_finetune_skyscrapers.ipynb

## Important

If you create a dataset using the OpenAI API you need to make sure you comply with their Terms of Services and Policies if you intend to distribute it

https://openai.com/it-IT/policies/usage-policies

https://openai.com/it-IT/policies/terms-of-use

## Setup

To be able to run this code you have to set an environment variable OPENAI_API_KEY with your actual OpenAI API key

You will also need a textfile containing the prompt to be used every image in the dataset. For instance, suppose you want to create a dataset of black cats, the textfile would contain something like:

"A photorealistic picture of a black cat."

The default image generation model is currently dalle-2, but I would recommend to use dalle-3 if you have the budget

## Running the code

The entry point for this repo is `generate_dataset.py`


## Other

Add about unicode replacement