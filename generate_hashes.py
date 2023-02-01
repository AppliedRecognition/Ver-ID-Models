from hashlib import sha256
import os
import json

root_dir = os.path.dirname(__file__)
files_dir = os.path.join(root_dir, 'files')
files = os.scandir(files_dir)
hashes = {}
for file in files:
    if file.is_file():
        with open(file.path, 'rb') as f:
            hash = sha256()
            hash.update(f.read())
            digest = hash.hexdigest()
            hashes[os.path.relpath(file.path, root_dir)] = digest
print(json.dumps(hashes, indent=4))