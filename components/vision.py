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
            self.sock.connect(("10.32.99.73", 1182))
        except:
            return None

    def getData(self):
        # if socket has closed, except: will run
        try:
            self.sock.send(b'\r\n')
            data = self.sock.recv(256)
            data = data.decode("utf-8") # info comes back as a byte string
            data = data.strip() # remove any whitespace

            if (data.find(",") == -1): # no data
                print("Nothing")
                return False
            else:
                data = data.split(',')

                i = 0
                for a in data:
                    if (i == 3):
                        a = a.replace(':','')

                    data[i] = float(a)
                    i = i + 1

                return data

        except: # re-opens the socket
            self.__init__()
