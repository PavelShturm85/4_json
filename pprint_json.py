import sys
import json


def load_data(enter_file):
    with open(enter_file) as json_file:
        json_content = json.load(json_file)
    return json_content


def pretty_print_json(uploaded_data):
    pretty_content = json.dumps(uploaded_data,
                                sort_keys=True,
                                indent=4,
                                ensure_ascii=False)
    return print(pretty_content)


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    pretty_print_json(data)
