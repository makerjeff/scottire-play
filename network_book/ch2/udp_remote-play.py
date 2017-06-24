import random, socket, sys
from jwxcolors import jwxcolors as jwxc

# GLOBAL VARS
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060

# SERVER LOGIC
if len(sys.argv) >= 2 and sys.argv[1] == 'server':
    print jwxc.BLUE + 'initializing server' + jwxc.ENDC

    s.bind(('127.0.0.1', PORT))
    #TODO: continue here.


# CLIENT LOGIC
elif len(sys.argv) >= 2 and sys.argv[1] == 'client':
    print jwxc.PURPLE + 'starting up client' + jwxc.ENDC

# ERROR-OR LOGIC
else:
    print jwxc.YELLOW + 'usage: udp_remote-play.py server | client' + jwxc.ENDC