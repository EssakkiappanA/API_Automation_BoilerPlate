import json
import os.path


def read_json(filename):
    file_name = filename+".json"
    file_dir = os.path.join(os.getcwd(), "test_data","body_data")
    file_path = os.path.join(file_dir, file_name)
    with open(file_path) as f:
        data = json.load(f)
    return data
