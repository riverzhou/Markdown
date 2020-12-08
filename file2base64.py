#!/usr/bin/env python3

import sys
from base64 import b64encode

with open(sys.argv[1], 'rb') as f:
    b64 = b64encode(f.read()).decode()
    print(('\n[{}]:data:image/png;base64,'.format(sys.argv[1]))+b64+'\n')
