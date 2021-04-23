import argparse
from json2csv.json2csv import main


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a JSON file to CSV')
    parser.add_argument('-i',
                        '--jsonfile',
                        metavar='jsonfile',
                        type=str,
                        required=True,
                        help='the path to the JSON file to convert')

    parser.add_argument('-o',
                        '--output-path',
                        metavar='csvfile',
                        type=str,
                        required=True,
                        help='the path where the CSV file will be written to')

    args = parser.parse_args()

    main(args)
