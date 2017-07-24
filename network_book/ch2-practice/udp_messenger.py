import socket, sys, os
import jwxcolors

# TODO:
# instance socket
# configure socket
# switch for client or server
# if server
# if client

# Network basics:
# create socket
# set PORT, SERVER, MAXBYTES

# SERVER:
# bind
# recvfrom(MAX)
# whileTrue
# data, addr = s.recvfrom(MAX)
# sendto(<message>, <sendto addr>)

# CLIENT:
# sendto(data, addr)
# data, addr = s.recvfrom(MAX)

# -----------------------------

os.system('clear')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535 # max packet size
PORT = 1060
SERVER = ('127.0.0.1', PORT)    # local server

# IF SERVER
if sys.argv[1:] == ['server']:
    s.bind(SERVER)
    print 'Listening at', s.getsockname()

    while True:
        data, addr = s.recvfrom(MAX)    # split data here if needed.
        print 'The client at', addr, 'says', repr(data) #repr() returns a printable version of any object.
        s.sendto('Your data was %d bytes' % len(data), addr)

# IF CLIENT
elif sys.argv[1:] == ['client']:

    total_message = 1
    mydata = raw_input('Enter your message: ')

    while mydata != 'q':
        os.system('clear')

        print 'Address before sending:', s.getsockname()
        s.sendto(mydata, ('127.0.0.1', PORT))    # send to server instance
        print 'Address after sending:', s.getsockname()

        data, addr = s.recvfrom(MAX)

        print 'The server', addr, 'says', repr(data)

        total_message = total_message+1
        mydata = raw_input('Enter message #' + str(total_message) + ' (\'q\' to quit): ')


else:
    print >> sys.stderr, jwxcolors.jwxcolors.RED + 'usage: udp_messenger.py server|client' + jwxcolors.jwxcolors.ENDC

