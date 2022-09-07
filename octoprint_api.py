#!/usr/bin/python3

import os
import os.path
import sys
import socket
import requests
import json
import configparser

from pprint import pprint

def port_open(host, port):
  port_open = False
  try:
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if (a_socket.connect_ex((host, port)) == 0):
      port_open = True
    else:
      port_open = False
  finally:
    a_socket.close()
  return port_open

def get_printer_printing(host, port, api_key):
  response = requests.get("http://" + host + ":" + str(port) + '/api/printer', headers={"X-Api-Key":api_key})
  json = response.json()
  if 'error' in json:
    return False
  return json['state']['flags']['printing']

config = configparser.ConfigParser()
config.read('octoprint.conf')

def get_any_printing():
  host = '127.0.0.1'
  any_printing = False
  for port in range(int(config['Ports']['port_start']),int(config['Ports']['port_end'])):
    if(port_open(host, port)):
      key = 'key' + str(port)
      if key not in config['API']:
        print("Key missing in cofiguration for: http://" + host + ':' + str(port))
        sys.exit(1)
      if(get_printer_printing(host, port, config['API'][key])):
        any_printing = True
        break
  return any_printing
