import json
import glob
import sys
import os
from shutil import copy
import requests

# Use http to get config
response = requests.get('http://127.0.0.1:5000/getConfig/abc')
config = json.loads(response.content).get('config', {})

dir_path = config.get('dir_path', '')
file_type = config.get('file_type', 'csv')
targeted_files = glob.glob('{}*.{}'.format(dir_path, file_type))

if not len(targeted_files) or len(targeted_files) > config.get('file_number', 0):
    sys.exit()

for fname in targeted_files:
    statinfo = os.stat(fname)
    if statinfo.st_size/1024 > config.get('file_size', 0):
        sys.exit()

    copy(fname, '/home/oak/mysimbdp-client-dir/abc/')
