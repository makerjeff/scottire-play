import random, socket, sys
from jwxcolors import jwxcolors as jwxc


# SERVER LOGIC
if len(sys.argv) >= 2 and sys.argv[1] == 'server':
    print jwxc.BLUE + 'initializing server' + jwxc.ENDC

# CLIENT LOGIC
elif len(sys.argv) >= 2 and sys.argv[1] == 'client':
    print jwxc.PURPLE + 'starting up client' + jwxc.ENDC

# ERROR-OR LOGIC
else:
    print jwxc.YELLOW + 'usage: udp_remote-play.py server | client' + jwxc.ENDC