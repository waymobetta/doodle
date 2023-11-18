#!/usr/bin/env python3

import os
import sys
import subprocess
from os import listdir
from doodle_config import cfg
from os.path import isfile, join, splitext

# @title: execute_shell_cmd
# @param: name: string
# @param: json_path: string path to output JSON records
def execute_shell_cmd(name,json_path):
    # craft output path to JSON record
    json_full_path = '{}/{}_journal.json'.format(json_path,name)
    
    # craft payload list for subprocess
    payload = ['jrnl', name, '--export', 'json', '-o', json_full_path]
    
    # if default jrnl
    if name == 'journal':
        # craft custom path to output JSON record
        json_full_path = '{}/{}.json'.format(json_path,name)
        # craft custom payload list for subprocess
        payload = ['jrnl', '--export', 'json', '-o', json_full_path] 

    # execute process
    process = subprocess.Popen(payload,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True)
    # read to STDOUT
    output = process.stdout.readline()
    print(output.strip())
   
# @title: export_jrnl_to_json: 
def export_jrnl_to_json():
    # read path to all jrnl txt records
    txt_path = cfg['jrnl_txt_path']
    # read path to all jrnl JSON records
    json_path = cfg['jrnl_json_path']

    # credit https://stackoverflow.com/a/3207973/7253829 
    # loop over directory contents
    # retrieve only files
    files=[f for f in listdir(txt_path) if isfile(join(txt_path,f))]
   
    # loop over files
    for file_name in files:
        # strip file extension
        file_name_stripped, _ = splitext(file_name)
        # split to get jrnl name
        jrnl_name_split = file_name_stripped.split('_')
        # execute shell cmd
        execute_shell_cmd(name=jrnl_name_split[0],json_path=json_path)  

# invoke
export_jrnl_to_json()
