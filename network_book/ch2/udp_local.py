#!/usr/bin/env python
# Chapter 2 UDP Local
# UDP client and server on local host

import socket, sys
import bcolors

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060
SERVER = ('127.0.0.1', PORT)

# check first input argument array to see if it's server or client
if sys.argv[1:] == ['server']:
    s.bind(SERVER)
    print 'Listening at', s.getsockname()

    while True: #runs forever
        data, addr = s.recvfrom(MAX)
        print 'The client at', addr, 'says', repr(data)
        s.sendto('Your data was %d bytes' % len(data), addr)

elif sys.argv[1:] == ['client']:
    print 'Address before sending:', s.getsockname()
    s.sendto('This is my message.', ('127.0.0.1', PORT))
    print 'Address after sending:', s.getsockname()

    data, addr = s.recvfrom(MAX) #overly promiscuous - see text! (?what?)

    print 'The server', addr, 'says', repr(data)

else:
    print >> sys.stderr, bcolors.bcolors.FAIL+'usage: udp_messenger.py server|client'+bcolors.bcolors.ENDC

