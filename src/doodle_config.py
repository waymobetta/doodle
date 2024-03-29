#!/usr/bin/env python3

import os

cfg = {
        # jrnl CLI sets this: /Users/USER/.config/jrnl/jrnl.yaml
        'jrnl_config_path': os.environ['JRNL_CONFIG_PATH'],
        # jrnl CLI sets this: /Users/USER/.local/share/jrnl/
        'jrnl_txt_path': os.environ['JRNL_TXT_PATH'],
        # /Users/USER/jrnl-data/
        'jrnl_json_path': os.environ['JRNL_JSON_PATH']
        }

