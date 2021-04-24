import csv
import json
from typing import Union


def convert(infile, outfile):
    data = load_json(infile)
    to_csv(data, outfile)


def load_json(filepath: str) -> Union[dict, list]:
    """
    Loads JSON file and returns either a dictionary or list.

    :param filepath: The filepath to the JSON file to load
    :return: A dict or list of the loaded JSON
    """
    with open(filepath) as fh:
        return json.load(fh)


def to_csv(data: Union[dict, list], filepath: str) -> None:
    """
    Takes a dict or list of dicts and outputs to CSV.

    :param data: The data to write out to CSV
    :param filepath: The filepath to output the data to
    """
    with open(filepath, 'w') as csvfile:

        if isinstance(data, dict):
            fieldnames = data.keys()
        elif isinstance(data, list):
            fieldnames = data[0].keys()
        else:
            fieldnames=None

        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        if isinstance(data, dict):
            csv_writer.writerow(data)
        elif isinstance(data, list):
            csv_writer.writerows(data)
