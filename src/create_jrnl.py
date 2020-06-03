#!/usr/bin/env python3

import sys
import yaml
from doodle_config import cfg

# @title: edits jrnl.yaml to add additional jrnl path
# @param: name: string 
def add_jrnl(name):
        # load jrnl.yaml from config
        yaml_path = cfg['jrnl_config_path']
        # load default jrnl txt directory
        jrnl_path = cfg['jrnl_txt_path']
        # format path to include custom jrnl name
        jrnl_path = '{}{}_journal.txt'.format(jrnl_path,name)
        # create new jrnl object for yaml 
        new_jrnl = {name: jrnl_path}
        
        # open jrnl.yaml to preview data structure
        with open(yaml_path, 'r') as yaml_file:
            try:
                # load yaml file
                yaml_data = yaml.safe_load(yaml_file)
                # propose update yaml file with path of new jrnl txt
                yaml_data['journals'].update(new_jrnl)
                # open jrnl.yaml to write updated data
                with open(yaml_path, 'w') as yaml_file2:
                    # dump updated data structure into yaml
                    yaml.safe_dump(yaml_data, yaml_file2)
            except yaml.YAMLError as e:
                print(e)

# check to ensure jrnl name passed
if len(sys.argv) < 2:
    print('usage: create_jrnl.py \'new_jrnl\'')
    sys.exit(1)

# set name of new jrnl
name=sys.argv[1]
# invoke
add_jrnl(name)
