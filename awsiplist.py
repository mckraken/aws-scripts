#!/usr/bin/python

from __future__ import print_function
import netaddr
import json
import requests
import sys

region = sys.argv[1]

aws_ip_list_d = json.loads(requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').text)

ip_region_l = [net['ip_prefix'] for net in aws_ip_list_d['prefixes'] if net['region'] == region]

aws_merged_ip_l = [str(net) for net in netaddr.cidr_merge(ip_region_l)]

for item in aws_merged_ip_l:
    print(item)

