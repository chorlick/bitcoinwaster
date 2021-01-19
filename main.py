

server_time_url="https://api.kraken.com/0/public/Time"


import krakenex
import logging
import threading
import time
import pandas
import msvcrt
import sys
from enum import Enum
import ta
import sqlite3
import sqlalchemy


class BitChop : 
   

    def console_print(self, text, new_line = "\r") :
        print(text, end=new_line)
        sys.stdout.flush()

if __name__ == "__main__":
    bc = BitChop()
    bc.start()
    logging.info("Main application shutdown")