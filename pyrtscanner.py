#!/usr/bin/env python
# a very simple python 2.x port scanner and banner grabber
# by jcas1 https://github.com/jcas1
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Have to update raw input to input for python 3 and eval
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in range(1,1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set timeout to speed up the scan
        sock.settimeout(0.2)
        result = sock.connect_ex((remoteServerIP, port))
# If result (port) open (0) try and get data
        if result == 0:
             try:
# Grab the banner if socket connection sending data
                  banner = sock.recv(104096)
# Print port number
                  print "Port {}:      Open".format(port)
# Print banner
                  print banner
# if no data sent but the port is open, print a port open message before closing the connection
             except socket.error:
                 print "Port {}:      Open, but it sent no data :(".format(port)
                 sock.close()
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname {} could not be resolved. Exiting'.format(remoteServer)
    sys.exit()

except socket.error:
    print "Couldn't connect to server on {}:".format(port)
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
