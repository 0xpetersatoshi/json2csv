"""
This module contains helper functions for the json2csv package.
"""

import collections
from typing import Union


def _is_dict(data: Union[dict, list]) -> bool:
    """
    Checks whether provided data structure is a dictionary or not.

    :param data: The data to check
    :return: true if is dict, false otherwise
    """
    if isinstance(data, dict):
        return True

    return False


def _flatten(data: dict, parent_key: str = '', sep: str = '_') -> dict:
    """
    Flattens nested dictionaries.

    :param data: The dictionary to flatten
    :param parent_key: The name of the new key in the flattened dictionary
    :param sep: The separator to use in the parent_key name
    :return: A flattened dictionary
    """
    items = []
    for key, value in data.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, collections.MutableMapping):
            items.extend(_flatten(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def flatten_data(data: Union[dict, list]) -> Union[dict, list]:
    """
    Flattens a dictionary or list of dictionaries.

    :param data: The list or dictionary to flatten
    :return: A flattened dictionary or list of flattened dicts
    """
    if _is_dict(data):
        return _flatten(data)

    return [_flatten(item) for item in data]


def extract_data(data: Union[dict, list], datakey: str) -> Union[dict, list]:
    """
    Extracts data to convert to CSV from multi-nested response.

    :param data: The list or dictionary to extract data from
    :param datakey: The fieldname to use to extract data from the dictionary
    :return: A subset of the original data passed in in the form of dict
        or list of dicts
    """
    try:
        if _is_dict(data):
            return data[datakey]

        return [item[datakey] for item in data]
    except KeyError as error:
        print(f'Error: {error}')
        raise KeyError from error
