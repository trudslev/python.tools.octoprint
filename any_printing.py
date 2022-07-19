#!/usr/bin/python3

import octoprint_api
import sys

if(octoprint_api.get_any_printing() == True):
  sys.exit(1)
else:
  sys.exit(0)
