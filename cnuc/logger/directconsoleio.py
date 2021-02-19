#python imports
import time 

#bitwaster imports

class DirectConsoleIo : 
    format = "{}:%(asctime)s: %(message)s"
    
    def error(self, message, end="\n") : 
        print ("Error:{}: {}".format(time.asctime(), message,  end=end))

    def info(self, message, end="\n") : 
        print ("Info:{}: {}".format( time.asctime() ,message , end=end))

    def debug(self, message, end='\n') :
        print ("Debug:{}: {}".format( time.asctime() ,message , end=end))
