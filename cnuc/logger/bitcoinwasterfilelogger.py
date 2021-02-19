#python imports
import logging
import sys
import logging.handlers

#bitcoinwaster imports

class BitcoinWasterFileLogger :
        log_handler = None
        logger = None
        def __init__(self, logging_config) :
                logFilePath = logging_config['path']
                self.logger = logging.getLogger('bitcoinwaster-filelogger')
                self.log_handler =  logging.handlers.TimedRotatingFileHandler(
                    filename=logFilePath, when='midnight', backupCount=30)
                if logging_config['level'] == 'debug':
                        self.logger.setLevel(logging.DEBUG)
                elif logging_config['level'] == 'info':
                        self.logger.setLevel(logging.INFO)
                formatter = logging.Formatter('%(asctime)s | %(name)s |  %(levelname)s: %(message)s')
                self.log_handler.setFormatter(formatter)
                self.logger.addHandler(self.log_handler)
                self.logger.info("file logger started")

        def debug(self, message):
                self.logger.debug(message)

        def info(self, message):
                self.logger.info(message)

