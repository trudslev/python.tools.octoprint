#!/usr/bin/python3

import octoprint_api
import os

if(octoprint_api.get_any_printing() == False):
  os.system('reboot')
