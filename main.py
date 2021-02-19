#python imports
import argparse

#bitwaster imports
import cnuc.bcstrings 
from cnuc.bitcoinwaster import BitcoinWaster
from cnuc.bitcoinwasterdaemon import BitcoinWasterDaemon

if __name__ == "__main__":
    
    #start with argument parsing
    parser = argparse.ArgumentParser(description=cnuc.bcstrings.BITWASTER_DESCRIPTION)
    parser.add_argument('-c', '--configuration', type=str, metavar="CONFIGURATION", help='path to configuration file', required=True)
    parser.add_argument('-d', '--debug', type=str, metavar="DEBUG", help='debug level for bitwaster(default info)', default='info')
    args = parser.parse_args()

    client = BitcoinWaster(args)
    client.start()