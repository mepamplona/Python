#!/usr/bin/env python
#File: modscan.py
#Desc: Modbus TCP Scanner
#version: 0.1

import socket
import sys

def main(self):
    if len(sys.argv) != 2:
        print "usage: modscan <rangeIP>"
    else:
        print "Se ejecutaria el programa %s" %self


if __name__ == '__main__':
    try: main(sys.argv[1])
    except KeyboardInterrupt:
        print "Scan canceled by user."
        print "Thank you for using ModScan"
    except:
        sys.exit()
