#import system libs
import os

class BitcoinWasterGlobals:

    @classmethod
    def plugin_directory(cls):
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/plugins"

    @classmethod
    def keys_directory(cls):
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/keys"