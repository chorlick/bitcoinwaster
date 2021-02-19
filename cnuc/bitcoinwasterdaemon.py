
import sys
import os
import socketserver
import threading
import select
import daemon
import fcntl

from cnuc.bitcoinwasterrequesthandler import BitcoinWasterRequestHandler

DAEMON_PIPE = "/tmp/bcw-pipe"
class BitcoinWasterDaemon : 
    args = None
    thread = None
    running = False
    logger = None

    def __init__(self, logger) : 
        self.logger = logger

    def start (self):
        self.thread = threading.Thread(target=self.start_server)
        self.thread.start()

    def start_server(self) :
        self.running = True
        if not os.path.exists(DAEMON_PIPE) :
            os.mkfifo(DAEMON_PIPE)
        else :
            os.remove(DAEMON_PIPE)
            os.mkfifo(DAEMON_PIPE)

        r = os.open(DAEMON_PIPE,  os.O_RDWR | os.O_NONBLOCK)
        buffer = ""
        while self.running : 
            read, write, excepts = select.select([r], [], [], 1/10)
            if r in read:
                c = os.read(r, 1).decode("utf-8")
                if c == '\n' : 
                    print(buffer)
                    buffer = ""
                buffer += c
        self.logger.info("kill command received")

    def shutdown(self) :
        self.running = False