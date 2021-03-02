import json


def get_data(filename):
    with open(filename) as file:
        return json.load(file)

