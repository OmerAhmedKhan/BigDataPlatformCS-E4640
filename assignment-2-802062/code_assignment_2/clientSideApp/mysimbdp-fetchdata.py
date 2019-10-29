import json
import glob
import sys
import os
from shutil import copy


with open('configuration.json', 'r') as f:
    config = json.load(f)

dir_path = config.get('abc', {}).get('dir_path', '')
file_type = config.get('abc', {}).get('file_type', 'csv')
targeted_files = glob.glob('{}*.{}'.format(dir_path, file_type))

if not len(targeted_files) or len(targeted_files) > config.get('abc', {}).get('file_number', 0):
    sys.exit()

for fname in targeted_files:
    statinfo = os.stat(fname)
    if statinfo.st_size/1024 > config.get('abc').get('file_size', 0):
        sys.exit()

    copy(fname, '/home/oak/mysimbdp-client-dir/abc/')
