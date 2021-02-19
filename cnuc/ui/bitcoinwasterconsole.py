import sys

import cnuc.ui.windowsconsole
import cnuc.ui.linuxconsole

class BitcoinWasterConsole : 
     console = None
     platform = None
     def __init__(self) :
          if sys.platform == "win32" :
               self.console =  cnuc.ui.windowsconsole.WindowsConsole()
          if sys.platform == 'linux':
               self.console =  cnuc.ui.linuxconsole.LinuxConsole()

     def start(self) :
          self.console.start()