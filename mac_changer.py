#!/usr/bin/env python

import subprocess
import optparse
from optparse import OptionParser

parser: OptionParser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
newmac = options.new_mac
print(f"You set {newmac} for the {interface} interface")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
subprocess.call(["ifconfig", interface, "up"])
