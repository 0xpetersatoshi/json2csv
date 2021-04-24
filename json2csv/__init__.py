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

    args = parser.parse_args()
    convert(args.jsonfile, args.csvfile)


if __name__ == '__main__':
    main()
