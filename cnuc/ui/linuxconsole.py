import time
import socket 
import sys
import os
import selectors
import select
import threading
from subprocess import Popen, PIPE
import subprocess
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import VSplit, Window, FloatContainer, Float
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout


DAEMON_IN_PIPE = "/tmp/daemon-in-pipe"
DAEMON_OUT_PIPE = "/tmp/daemon-out-pipe"

class LinuxConsole:
    running = None
    console_window = None
    buffer = ""
    socket = None
    read_thread = None
    inputs = []
    outputs = []
    excepts = []
    fp_read = None
    fp_write = None

    def __init__(self):
        self.running = False
        
    def start(self):
        pass