import json
import random
import datetime
import csv

from unidecode import unidecode


def write_json_as_csv(json_in, csv_out):

    with open(csv_out, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['file_name','text'])

        for k in json_in.keys():
            text = unidecode(json_in[k])
            assert text.isascii()
            csv_writer.writerow([k, text])


def load_from_csv(csv_file):

    meta = {}
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Read column headers
        for row in reader:
            meta.update({row[0]: row[1]})

    return meta


def generate_filename():
    return datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S_" + str(random.randint(0, 1000)) + '.png')
