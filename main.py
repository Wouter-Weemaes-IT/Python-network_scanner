#!/usr/bin/env python3
import protocol_scanner as PS
import live_scanner as LS
import host_sum as HS
from scapy.all import *



selection = input("1. protocol scanner\n2. live scanner\n3. host sum\n:")

if selection == "1": 
    sniff(iface="en0", prn=PS.handler, store=0)

if selection == "2": 
    sniff(iface="en0", prn=LS.handler, store=0)

if selection == "3": 
    sniff(iface="en0", prn=HS.handler, store=0)




