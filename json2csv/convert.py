"""
This module takes the arguments provided from the CLI and converts a JSON
file to CSV.
"""

import csv
import json
from pathlib import Path
from typing import Union

from json2csv.transform import extract_data, flatten_data


def convert(infile: Path, outfile: Path, flatten: bool = False, datakey: str = None) -> None:
    """
    Converts provided JSON file into a CSV file.

    :param infile: Path object containing the path to the JSON file
    :param outfile: Path object where the CSV file will be written to
    :param flatten: Boolean value to determine if nested data should be flattened
    :param datakey: String representing field name in nested structure used to extract data
    """
    with open(infile) as jsonfile:
        data = json.load(jsonfile)

    if datakey:
        data = extract_data(data, datakey)

    if flatten:
        data = flatten_data(data)

    # Create default output filepath if none provided
    if outfile is None:
        outfile = infile.parent / 'data.csv'

    to_csv(data, outfile)


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

    print(f"CSV file written to {filepath}")
