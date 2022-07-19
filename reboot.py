#!/usr/bin/python3

import octoprint_api

from pprint import pprint

if(octoprint_api.get_any_printing() == False):
  os.system('reboot')
