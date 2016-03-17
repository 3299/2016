"""
Communicates with the Raspberry Pi to get tracking info about the target. Usage:
vision = Vision()
print(vision.getData())
"""

import socket

class Vision(object):
    def __init__(self):
        # open socket
        try:
            self.sock = socket.socket()
            self.sock.connect(("raspberrypi", 1182))
        except:
            return None

    def getData(self):
        # if socket has closed, except: will run
        try:
            self.sock.send(b'\r\n')
            data = self.sock.recv(256)
            data = data.decode("utf-8") # info comes back as a byte string
            return data
        except: # re-opens the socket then requests data again
            self.__init__()
            return self.getData()
