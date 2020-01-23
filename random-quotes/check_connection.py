import socket
from constants import CONN_URL

def is_connected():
    try:
        socket.create_connection((CONN_URL, 80))
        return True
    except OSError:
        pass
    return False
