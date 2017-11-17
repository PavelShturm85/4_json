import sys
import json


def load_data():
    got_data = open(input_file(), 'r')
    json_content = json.load(got_data)
    return json_content


def pretty_print_json():
    ppj = json.dumps(load_data(), sort_keys=True, indent=4, ensure_ascii=False)
    return print(ppj)


if __name__ == '__main__':
    def input_file():
        if len(sys.argv) > 1:
            return sys.argv[1]
        else:
            return input("input file name.json: ")

    pretty_print_json()
