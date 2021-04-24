import argparse
from pathlib import Path

from json2csv.convert import convert

def main():
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
