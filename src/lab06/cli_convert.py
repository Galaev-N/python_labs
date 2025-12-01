import argparse
import sys

sys.path.append(r"/Users/galaevka/python_labs-3/src/lab05")
from json_csv import json_to_csv, csv_to_json
from csv_to_xlsx import csv_to_xlsx

# python3 /Users/galaevka/python_labs-3/src/lab06/cli_convert.py json2csv --in /Users/galaevka/python_labs-3/data/lab06/in/lol.json --out /Users/galaevka/python_labs-3/data/lab06/out/new.csv
# python3 /Users/galaevka/python_labs-3/src/lab06/cli_convert.py csv2json --in /Users/galaevka/python_labs-3/data/lab06/in/lol.csv --out /Users/galaevka/python_labs-3/data/lab06/out/new.json
# python3 /Users/galaevka/python_labs-3/src/lab06/cli_convert.py csv2xlsx --in /Users/galaevka/python_labs-3/data/lab06/in/lol.csv --out /Users/galaevka/python_labs-3/data/lab06/out/new.xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)

    elif args.cmd == "scv2json":
        csv_to_json(args.input, args.output)

    else:
        csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()
