
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>
api_requests_example.py
Illustrate the following concepts:
- Making REST API calls using requests library
- Intended to be entered into an interactive
  interpreter
"""

import pyang
import json
import requests
from pprint import pprint
router = {"ip": "ios-xe-mgmt.cisco.com",
	       "port": "9443",
           "user": "developer",
           "pass": "C1sco12345"}

headers = {"Accept": "application/yang-data+json",
           "Content_Type":"application/yang-data+json"}

u = "https://{}:{}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

u = u.format(router["ip"], router["port"])

r = requests.get(u,headers = headers,auth=(router["user"], router["pass"]),verify=False)

#pprint(r.text)


api_data = r.json()

update ={'ietf-interfaces:interface': {'description': 'Configured by theepan',
                               'enabled': True,
                                'ietf-ip:ipv4': {'address': [{'ip': '10.255.255.2',
                                                             'netmask': '255.255.255.0'}]},
                                'ietf-ip:ipv6': {},
                                'name': 'GigabitEthernet2',
                                'type': 'iana-if-type:ethernetCsmacd'}}

headput = {"Content_Type":"application/yang-data+json"}

s = requests.post(u,data=json.dumps(update),headers = headput,auth=(router["user"], router["pass"]),verify=False,).json()

pprint(s.text)








