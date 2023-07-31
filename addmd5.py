#!/usr/bin/env python

import sys
import os
import json
import tempfile

import sys

root = sys.argv[1]

import hashlib

md5_upf = hashlib.md5(open(root + ".upf", 'rb').read()).hexdigest()
md5_psml = hashlib.md5(open(root + ".psml", 'rb').read()).hexdigest()

