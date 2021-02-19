import time
import socket 
import sys
import os
import selectors


serverAddressPort   = ("127.0.0.1", 7000)
bufferSize          = 1024
msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)



class WindowsConsole:
    running = None
    console_window = None
    buffer = ""
    socket = None

    def __init__(self):
        self.running = False
        

    def start(self):
        self.running = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(serverAddressPort)
        while self.running : 
            buffer = input()
            self.socket.sendall(str.encode(buffer))
            print("tryig to read")
            msgFromServer = self.socket.recv(10)
            print("reads")
            msg = "{}".format(msgFromServer[0])
            print(msg)

    def shutdown(self):
        running = False

