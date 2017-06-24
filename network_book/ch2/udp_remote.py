#!/usr/bin/env python
# Foundations of Python network programming - Chapter 2 - udp_remote.py
# UDP client and server for talking over the network.

import random, socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535 # max packet size.
PORT = 1060

# TYPE OF SERVER START UP LOGIC 1 (server)
if 2 <= len(sys.argv) <= 3 and sys.argv[1] == 'server':

    # ? study.
    interface = sys.argv[2] if len(sys.argv) > 2 else ''

    s.bind((interface, PORT))
    print 'Listening at', s.getsockname()

    while True:
        data, addr = s.recvfrom(MAX)

        # coin flip
        if random.randint(0, 1):
            print 'The client at', addr, 'says:', repr(data)
            s.sendto('Your data was %d bytes' % len(data), addr)

        else:
            print 'Pretending to drop packet from', addr

# TYPE OF SERVER START UP LOGIC 2 (client)
elif len(sys.argv) == 3 and sys.argv[1] == 'client':
    hostname = sys.argv[2]
    s.connect((hostname, PORT))

    print 'Client socket name is', s.getsockname()

    delay = 0.1

    while True:
        s.send('This is another message.')
        print 'Waiting up to', delay, 'seconds for a reply.'
        s.settimeout(delay)

        try:
            data = s.recv(MAX)

        except socket.timeout:
            delay *= 2 # wait even longer for the next request.

            if delay > 2.0:
                raise RuntimeError('I think the server is down.')

        except:
            raise   # a real error, reveal to user.

        else:
            break   # done, break out of the while loop

    print 'The server says', repr(data)

# TYPE OF SERVER START UP LOGIC 3 (fallback)
else:
    print >> sys.stderr, 'usage: udp_remote.py server [ <interface> ]'
    print >> sys.stderr, '   or: udp_remote.py client <host>'
    sys.exit(2)