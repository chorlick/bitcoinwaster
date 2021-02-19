# python imports
import json
from python_json_config import ConfigBuilder
from os import path
# bitwaster imports

from cnuc.logger.directconsoleio import DirectConsoleIo

class KeyboardMonitor:

    def user_keyboard_capture(self) : 
            logging.info("Starting user keyboard input thread")
            while self.running :
                input = msvcrt.getch()
                if input:
                    if input == b'\x03' : 
                        logging.info("User escape pressed")
                        self.shutdown()7+
                    if input == b'\r':
                        logging.debug("Command entered[{}]".format(self.buffer))
                        self.console_print("", "\n")
                        self.execute_user_command(self.buffer)
                        self.console_print(">", "")
                        self.buffer = ""

                    else :
                        decoded = input.decode('utf-8')
                        self.buffer += self.buffer.join(decoded)
                        self.console_print(decoded, "")
                else: 
                    logging.error("Strange keyboard thing happened...exiting")
                    exit(-1)

            logging.info("Keyboard thread shutdown")

    def execute_user_command(self, command) :
            logging.debug("running command {}".format(command))
            if command == "":
                return
            elif command == self.Commands.MACD:
                self.macd_algo()

            elif command == self.Commands.INDEX : 
                self.print_bc_indexes()
            elif command == self.Commands.STOP_POLL : 
                self.stop_bc_polling()
            else : 
                self.console_print("\nCommand not found", "") 