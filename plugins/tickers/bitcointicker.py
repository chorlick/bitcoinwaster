import krakenex

class BitcoinTicker:

    def __init__(self) :
        self.k = krakenex.API()
        self.k.load_key('kraken.key')

    def poll_bitcoin_price(self) :
        logging.info("Starting bitcoin polling thread")
        time.sleep(1)
        try:
            while self.bc_poll_flag:
                query = self.k.query_public('Ticker?pair=XBTUSD')
                if len(query['error']) > 0 : 
                    logging.error("Error returned from bc polling thread")
                    print(query['error'])
                    self.shutdown
                last_price = query['result']['XXBTZUSD']['a']
                last_price =last_price[0]
                b = bitcointick.BitcoinTick()
                b.create_from_kraken_json(query)
                self.bitcoindb.save(b)
                time.sleep(1)
            logging.info("Bitcoin polling thread shutdown")
        except Exception as e : 
            logging.error("Exception : {}".format(e))
