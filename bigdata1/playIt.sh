#!/bin/bash

sudo apt install virtualenv
mkdir /home/$USER/virtual_env
cd /home/$USER/virtual_env/
virtualenv -p python3 bigdata1
. bigdata1/bin/activate
cd /home/$USER/bigdata/
python3 setup.py install
python3 api.py
