"""JSON to CSV converter CLI tool

This script allows the user to provide a path to a JSON file and have
that file be converted to CSV format.

As JSON data can vary, there are some helpful arguments to deal with
different shapes of data. The --flatten argument will de-nest and
flatten nested data in the JSON file. Often times in JSON files,
the records can be nested within a top level key. This key can
be passed to the --data-key argument and the script will extract
the JSON records from this key and convert them to CSV.
"""

import argparse
from pathlib import Path

from json2csv.convert import convert

def main():
    """
    The entrypoint to the json2csv package.
    """
    parser = argparse.ArgumentParser(description='Convert a JSON file to CSV')
    parser.add_argument('-i',
                        '--jsonfile',
                        dest='jsonfile',
                        type=Path,
                        help='the path to the JSON file to convert')

    parser.add_argument('-o',
                        '--output-path',
                        dest='csvfile',
                        type=Path,
                        help='the path where the CSV file will be written to')

    parser.add_argument('-f',
                        '--flatten',
                        dest='flatten',
                        action='store_true',
                        help='flattens nested data structures')

    parser.add_argument('-k',
                        '--data-key',
                        dest='datakey',
                        type=str,
                        help='extracts nested data from JSON file to be converted into CSV')

    args = parser.parse_args()
    convert(args.jsonfile, args.csvfile, args.flatten, args.datakey)


if __name__ == '__main__':
    main()
