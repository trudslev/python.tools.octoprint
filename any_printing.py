#!/usr/bin/python3

import octoprint_api
import sys
import argparse
parser = argparse.ArgumentParser(description='Detect if any 3D printers are printing.')
parser.add_argument('-d', '--debug', action='store_true', default=False,
                    help='show debug information')

args = parser.parse_args()

if(octoprint_api.get_any_printing() == True):
  if(args.debug == True):
      print("At least one printer is printing");
  sys.exit(1)
else:
  if(args.debug == True):
      print("No printers are printing");
  sys.exit(0)
