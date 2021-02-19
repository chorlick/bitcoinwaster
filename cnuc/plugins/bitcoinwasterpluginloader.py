#import system libs
import importlib.util
import os

#import bitcoinwaster libs
from cnuc.bitcoinwasterglobals import BitcoinWasterGlobals

class BitcoinWasterPluginLoader :
    modules = []
    logger = None

    def __init__(self, logger) : 
        self.logger = logger

    def load_plugin (self, module_name, path, args) :
        try : 
            full_path = "{}/{}.py".format(BitcoinWasterGlobals.plugin_directory(), path)
            if not os.path.exists(full_path) :
                self.logger.info("module not found {}".format(full_path))
                return 
            self.logger.info("loading {} from {}".format(module_name, full_path))
            spec = importlib.util.spec_from_file_location(module_name, full_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            #self.modules.append(module)
        except Exception as e : 
            self.logger.debug("error loading module {} : {}".format(module_name, e))