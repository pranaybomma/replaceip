#!/usr/bin/python
# Author: Pranay Bomma
import sys
import re
from netaddr import *

iplist = list()
natlist = {}
with open("nat.txt", "r") as file:
    rows = ( line.split(' ') for line in file)
    natlist = { row[0].strip():row[1].strip() for row in rows }
    file = open ("ip.txt", 'r')
    print " "
    print "############# NATTED LIST ##################"
    print " "
    for networ in file:
        ip = IPNetwork(networ.strip())
        for i in ip:
            i = str(i)
            for item in natlist:
                if (re.match(i + '$',item)):
                    print natlist[item]
                    Natted_IP = natlist[item]
                    iplist.append(Natted_IP)
                else:
                    continue
print " "
print "###################### Merged IP ##################"
print " "
cidr = cidr_merge (iplist)
for result in cidr:
    print result
print " "
