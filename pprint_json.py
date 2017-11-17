import sys
import json


def input_file():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("input file name.json: ")


def load_data():
    enter_file = input_file()
    with open(enter_file) as json_file:
        json_content = json.load(json_file)
    return json_content


def pretty_print_json():
    uploaded_data = load_data()
    pretty_content = json.dumps(uploaded_data,
                                sort_keys=True,
                                indent=4,
                                ensure_ascii=False)
    return print(pretty_content)


if __name__ == '__main__':
    pretty_print_json()
