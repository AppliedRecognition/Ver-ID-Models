import json
import os
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    file_path = 'categories.json'
    json_data = load_json(file_path)
    missing_files = []
    for key, value in json_data.items():
        for k, v in value.items():
            for file in v:
                path = os.path.join('files', file)
                if not os.path.exists(path):
                    missing_files.append((key, k, file))
    if missing_files:
        for key, k, file in missing_files:
            sys.stderr.write(f"Missing file: {file} in category {key}/{k}\n")
        sys.exit(1)
    sys.stdout.write("Check successful\n")
    sys.exit(0)