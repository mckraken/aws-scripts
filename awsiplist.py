#!/usr/bin/python

from __future__ import print_function

import argparse
import json

import netaddr
import requests


def process_args():
    parser = argparse.ArgumentParser(
        description='Get list of Amazon IPs for a region.')
    parser.add_argument(
        'region', metavar="AWS_REGION",
        help='The region for which to get the IP list (e.g. us-west-1).')

    return parser.parse_args()

if __name__ == "__main__":
    region = process_args().region

    aws_ip_list_d = json.loads(
        requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').text)

    ip_region_l = [net['ip_prefix'] for net in aws_ip_list_d['prefixes']
                   if net['region'] == region]

    aws_merged_ip_l = [str(net) for net in netaddr.cidr_merge(ip_region_l)]

    for item in aws_merged_ip_l:
        print(item)
