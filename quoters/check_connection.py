import socket
from quoters.constants import CONN_URL

def is_connected():
    try:
        sock_conn = socket.create_connection((CONN_URL, 80))
        if(sock_conn):
            sock_conn.close()
        return True
    except OSError:
        pass
    return False
