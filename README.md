# json2csv

This is a simple CLI tool that converts a JSON file to CSV format.

## Installation

- Clone the repo
- cd into project folder
- run `pip install .`

## Basic Usage

### Simple

```bash
json2csv -i myfile.json
```

### JSON file has nested datastructures

```bash
json2csv -i myfile.json --flatten
```

This will recursively run through a JSON file and try and flatten nested datastructures.

### Needed data is nested within JSON structure

Example:

```json
{
  "results" : [
    {"key": "value"},
    {"key2": "value"},
    {"key3": "value"},
  ]
}
```

If you just need to convert the data contained in the "results" key, you can pass that key to the `--data-key` argument and the tool will extract that data and convert it to CSV.

```bash
json2csv -i myfile.json --date-key results
```

### Saving the output

By default, the CSV output file will be saved to the current directory from where the command is run. You can specify the output path and file name by using the `-o` argument.

```bash
json2csv -i myfile.json -o /tmp/mydata.csv
```
