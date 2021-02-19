
#python imports
import logging

#bitcoinwaster imports
from cnuc.logger.bitcoinwasterfilelogger import BitcoinWasterFileLogger
from cnuc.logger.bitcoinwasterconsolelogger import BitcoinWasterConsoleLogger

class BitcoinWasterLogger :
    agents = None 
    format = None

    def __init__(self) :
        self.agents = []

    def add_logger(self, logger_config) : 
        if logger_config["type"] == "file" :
            self.add_file_logger(logger_config)
        if logger_config["type"] == "console" :
            self.add_console_logger(logger_config)
    
    def add_console_logger(self, logger_config) :
        self.agents.append(BitcoinWasterConsoleLogger(logger_config))

    def add_file_logger(self, logger_config) :
        self.agents.append(BitcoinWasterFileLogger(logger_config))

    def info(self, message) :
        for agent in self.agents :
            agent.info(message)

    def debug(self, message) :
        for agent in self.agents :
            agent.debug(message)
