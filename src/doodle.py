#!/usr/bin/env python3

import os
import re
import sys
import json
import time 
import random
import argparse
from os import listdir
from haxor import haxor
from os.path import isfile, join
from doodle_config import cfg

# @title: read_file: reads specific jrnl file
# @param: name: string 
# @return: entry_list: list of entry objects
def read_file(name):
    # read path to custom jrnl in JSON format
    path = cfg['jrnl_json_path']

    # credit https://stackoverflow.com/a/3207973/7253829 
    # loop over directory contents
    # retrieve only files
    files=[f for f in listdir(path) if isfile(join(path,f))]
   
    # regex pattern for matching all custom journals
    # e.g. custom_journal.json
    pattern='{}_'.format(name)
    
    # loop over all journals
    for file_name in files:
        # match specific journal passed via flag
        if re.match(pattern,file_name):
            path+=file_name
            break
        # show default jrnl
        elif name=='Default':
            path+='journal.json'
            break
    # read entries of chosen jrnl
    with open(path,'r') as f:
        raw_entries=json.load(f)
        f.close()
    return raw_entries

# @title: combine_lists: combines title + body of entries
# @param: raw_entries: list of entry objects
# @param: date: date boolean
# @return: entry_list: list of formatted entries
def combine_lists(raw_entries,date):
        # list of entry strings
	entry_list=[]
        # loop over all entries in json file
	for entry in raw_entries['entries']:
            # combine body and title to create connected thought
            concat_entry='{} {}'.format(entry['title'].lower(),entry['body'].lower())
            # show date if flag passed
            if date:
                concat_entry='{}: {}'.format(entry['date'],concat_entry)
            # add entry to formatted list
            entry_list.append(concat_entry)
	return entry_list

# @title: read_entry: returns a random entry string from list of formatted entry objects
# @param: entry_list: list of formatted entry objects
# @param: last: previously returned entry string on last iteration
# @return: entry: single, random entry object within formatted list
# @return: last: return chosen entry string to be stored for comparison in future iteration
def rand_entry(entry_list,last):
    # choose random entry from formatted list of entry strings
    entry=random.choice(entry_list)
    # prevent repeating previously stored entry
    while entry==last:
        # choose new random entry entry from formatted list of entry strings
        entry=random.choice(entry_list)
    # store chosen entry as last entry for next iteration
    last=entry
    return entry,last

### ARGUMENTS
# parse arguments
parser=argparse.ArgumentParser('Doodle')
# argument to pass custom name of jrnl
parser.add_argument('-j','--journal',help='priv,default',required=False,default='Default')
# argument to pass optional date
parser.add_argument('-d','--date',help='display date',action='store_true',required=False,default=False)
# parse arguments
arguments=parser.parse_args()
# string: name of jrnl to read from
name=arguments.journal
# bool: flag to signal prefixing date to chosen entry
date=arguments.date

# anon function to clear terminal screen
clr=lambda:os.system('clear')

clr()
print('Doodling: '+name.title())

try:
    # init last entry string
    last=''
    # autopilot until ctrl^c
    while True:
        # get list raw entry objects
        raw_entries=read_file(name)
        # get list of formatted entry strings
        entry_list=combine_lists(raw_entries=raw_entries,date=date)
        # choose random entry string from list of formatted entry strings
        # set last value to avoid retrieving consecutive duplicates
        entry,last=rand_entry(entry_list=entry_list,last=last)
        # prevent rendering empty entries
        if len(entry) > 0: 
            # haxor prints text to STDOUT like a typewriter
            haxor(payload=entry,delay=0.05)
            # separate entry with carriage return
            print('',sep='\r')
except KeyboardInterrupt:
        # exit program with no error
	sys.exit(0)

