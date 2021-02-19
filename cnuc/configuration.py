# python imports
import json
from python_json_config import ConfigBuilder
from os import path
# bitwaster imports

from cnuc.logger.directconsoleio import DirectConsoleIo


class Configuration:
    config_url = None
    io = None
    builder = None
    config = None
    is_valid = None

    def __init__(self, config_url):
        self.config_url = config_url
        self.builder = ConfigBuilder()
        self.io = DirectConsoleIo()
        
        #add the required fields
        self.builder.set_field_access_required()

        self.builder.add_required_field('logging')
        self.builder.add_required_field('logging.writers')
        
        self.builder.add_required_field('database')
        self.builder.add_required_fields('database.db_url')

        self.builder.add_required_field('ticker_data_source')
        self.builder.add_required_field('ticker_data_source.source')

        self.builder.add_required_fields('plugins')

    def load_configuration(self):
        try:
            if not self.is_config_url_valid():
                self.configuration_error("Configuration file not found")
                return False
            self.config = self.builder.parse_config(self.config_url)
            if not self.validate_configuration() :
                return False
            else : 
                self.io.info("Configuration loaded")
                return True
        except Exception as e:
            self.configuration_error(e)

    def is_config_url_valid(self):
        try:
            return path.exists(self.config_url)
        except Exception as e:
            self.configuration_error(e)

    def configuration_error(self, e) :
        self.is_valid = False
        self.io.error("Loading configuration file.")
        self.io.error(e)

    def get_logging_config(self ):
        return self.config.logging.writers

    def get_plugin_config(self) : 
        return self.config.plugins

    def get_plugin_args(self)  : 
        return self.config.args

    def validate_configuration(self):
        try : 
            self.config.logging
            self.config.logging.writers
            self.config.database
            self.config.database.db_url
            self.config.plugins
            return True
        except Exception as e:
            self.io.error("Error validating configuration file ")
            self.io.error(e)


    def get_plugin_args_by_name(self, name) :
        if name in self.get_plugin_args().to_dict().keys():
            args = []
            index = list(self.get_plugin_args().to_dict().keys()).index(name)
            self.io.debug("index {}".format(index))
            vals  = list(self.get_plugin_args().to_dict().values())
            self.io.debug(vals[index])
            return vals[index]
        else : 
            self.io.error("plugin configuration not found for : {}".format(name))
            return -1