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
  return response.json()['state']['flags']['printing']

config = configparser.ConfigParser()
config.read('reboot.conf')

host = '127.0.0.1'
any_printing = False
for port in range(8080,8100):
  if(port_open(host, port)):
    key = 'key' + str(port)
    if key not in config['API']:
      print("Key missing in cofiguration for: http://" + host + ':' + str(port))
      sys.exit(1)
    if(get_printer_printing(host, port, config['API'][key])):
      any_printing = True
      break

if(any_printing == False):
  os.system('reboot')
