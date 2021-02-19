import threading
import socketserver 
import os 
import select 
import time

class BitcoinWasterRequestHandler(socketserver.StreamRequestHandler):

    data = ""
    running = False
    def handle(self):
        self.running = True
        print(self.connection)
        while self.running :
            time.sleep(100 / 1000)
            print(self.connection)
            self.data = self.rfile.readline().strip()

