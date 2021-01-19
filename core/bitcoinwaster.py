
class BitcoinWaster:
     mutex = None
    running = True
    logging = None
    k = None
    bc_polling_thread = None
    keyboard_input_thread = None
    bcdb_thread = None
    bc_poll_flag = True
    buffer = ""
    conn = None
    bitcoindb = None

    class Commands(str, Enum) :
        MACD = 'macd'
        INDEX = 'index'
        STOP_POLL = 'stop poll'
        START_POLL = 'start poll'

    def __init__(self) :
        self.k = krakenex.API()
        self.k.load_key('kraken.key')
        self.running = True
        self.bc_poll_flag = True
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
        self.bitcoindb = bitcoindb.BitcoinDb()

    def start(self) :
        logging.info("Starting threads")
        self.bc_polling_thread = threading.Thread(target=self.poll_bitcoin_price)
        self.keyboard_input_thread = threading.Thread(target=self.user_keyboard_capture)
        self.bcdb_thread = threading.Thread(target = self.bcdb_background_function)
        self.bcdb_thread.start()
        self.bc_polling_thread.start()
        self.keyboard_input_thread.start()
        logging.info("All threads started...")
        self.console_print(">", "")
        sys.stdout.flush()
        self.bc_polling_thread.join()
        self.keyboard_input_thread.join()
        self.bcdb_thread.join()

    def shutdown(self ):
        self.bc_poll_flag = False
        self.running = False
        self.bitcoindb.stop()

    


    def bcdb_background_function (self) : 
        self.bitcoindb.start()

    

 

    def stop_bc_polling(self) : 
        self.bc_poll_flag = False

    def print_bc_indexes(self):
        logging.info("Printing bitcoin indexs")

