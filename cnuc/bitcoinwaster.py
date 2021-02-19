#python modules
import argparse
import signal
import os
import time
from python_json_config import ConfigBuilder

#bitwaster modules
from cnuc.configuration import Configuration
from cnuc.logger.bitcoinwasterlogger import BitcoinWasterLogger
from cnuc.bitcoinwasterdaemon import BitcoinWasterDaemon
import cnuc.ui.bitcoinwasterconsole 
import cnuc.plugins.bitcoinwasterpluginloader as bitcoinwasterpluginloader


class BitcoinWaster:
    config = None
    config_url = None
    debug_level = None
    logger = None
    console = None
    daemon = None
    plugins = None

    def __init__(self, args) :
        self.config_url = args.configuration
        self.debug_level = args.debug
        self.logger  = BitcoinWasterLogger()

    def start(self) :
        self.start_signal_handlers()

        #self.console = cnuc.ui.bitcoinwasterconsole.BitcoinWasterConsole()
        #self.console.start()

        self.configuration = Configuration(self.config_url)
        
        self.load_configuration()
        if not self.configuration :
            return False
        
        for logger in self.configuration.get_logging_config() :
            self.logger.add_logger(logger)
        if not self.logger:
            return False

        self.logger.info("starting daemon")
        self.daemon = BitcoinWasterDaemon(self.logger)
        self.daemon.start()

        self.logger.info("all logging bootstraped")
        self.logger.info("loading plugins")   
        self.logger.debug(self.configuration.get_plugin_config().load.modules)
        self.plugin_loader = bitcoinwasterpluginloader.BitcoinWasterPluginLoader(self.logger)

        for plugin in self.configuration.get_plugin_config().load.modules :
            self.logger.debug("loading plugin {}".format(plugin['name']))
            args = self.configuration.get_plugin_args_by_name(plugin['name'])
            self.logger.debug(args)
            self.plugin_loader.load_plugin(plugin['name'], plugin['path'], args)
        self.daemon.thread.join()
        return True

    def start_signal_handlers(self) : 
        signal.signal(signal.SIGINT, self.sig_break_handler)
        
    def load_configuration(self) : 
        return self.configuration.load_configuration()

    def start_loggers(self) : 
        self.loggers = BitcoinWasterLogger()

    def shutdown(self ):
        pass

    def sig_break_handler(self, sign, frame) :
        self.daemon.shutdown()
        self.logger.info("shuting down")
        if os.path.exists("./daemon_runtime/bcw-pipe") :
            os.remove("./daemon_runtime/bcw-pipe")
        exit(0)
