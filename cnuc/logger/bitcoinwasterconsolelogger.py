#python imports
import logging
import sys
import os

#bitcoinwaster imports

DAEMON_IN_PIPE = "/tmp/daemon-in-pipe"
DAEMON_OUT_PIPE = "/tmp/daemon-out-pipe"

class BitcoinWasterConsoleLogger :
        log_handler = None
        logger = None
        def __init__(self, logging_config) :
                w = os.open(DAEMON_OUT_PIPE, os.O_RDWR)
                fd_w = os.fdopen(w, 'w')
                self.logger = logging.getLogger('bitwaster')
                self.log_handler = logging.StreamHandler()
                if logging_config['level'] == 'debug':
                        self.logger.setLevel(logging.DEBUG)
                elif logging_config['level'] == 'info':
                        self.logger.setLevel(logging.INFO)
                formatter = logging.Formatter('%(asctime)s | %(levelname)s: %(message)s')
                self.log_handler.setFormatter(formatter)
                self.logger.addHandler(self.log_handler)
                self.logger.info('console logger started')
                
        def debug(self, message):
                self.logger.debug(message)

        def info(self, message):
                self.logger.info(message)