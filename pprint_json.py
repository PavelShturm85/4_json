import sys
import json


def load_json_data(enter_file):
    with open(enter_file) as json_file:
        json_content = json.load(json_file)
    return json_content


def pretty_print_json(uploaded_data):
    pretty_content = json.dumps(uploaded_data,
                                sort_keys=True,
                                indent=4,
                                ensure_ascii=False)
    print(pretty_content)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Input filepath: ')
    content = load_json_data(input_file_name)
    pretty_print_json(content)
