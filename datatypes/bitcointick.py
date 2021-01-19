import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class BitcoinTick(Base):

    __tablename__ = 'bitcoin_tick'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    timestamp = sqlalchemy.Column(sqlalchemy.DateTime)
    ask = sqlalchemy.Column(sqlalchemy.Float)
    ask_lot = sqlalchemy.Column(sqlalchemy.Integer)
    bid = sqlalchemy.Column(sqlalchemy.Float)
    bid_lot = sqlalchemy.Column(sqlalchemy.Integer)
    last_closed = sqlalchemy.Column(sqlalchemy.Float)
    last_closed_lot = sqlalchemy.Column(sqlalchemy.Float)
    today_volume = sqlalchemy.Column(sqlalchemy.Float)
    last_day_volume = sqlalchemy.Column(sqlalchemy.Float)
    weighted_today_volume = sqlalchemy.Column(sqlalchemy.Float)
    weighted_last_day_volume = sqlalchemy.Column(sqlalchemy.Float)   
    today_trades = sqlalchemy.Column(sqlalchemy.Integer)
    last_day_trades = sqlalchemy.Column(sqlalchemy.Integer)
    today_low = sqlalchemy.Column(sqlalchemy.Float)
    last_day_low = sqlalchemy.Column(sqlalchemy.Float)
    today_high = sqlalchemy.Column(sqlalchemy.Float)
    last_day_high = sqlalchemy.Column(sqlalchemy.Float)
    open_price = sqlalchemy.Column(sqlalchemy.Float)

    def __repr__(self) : 
        return "<BitCoinTick(id={}, timestamp={}, ask={}, ask_lot={}, bid={}".format(self.id, self.timestamp, self.ask, self.ask_lot, self.bid)

    def create_from_kraken_json(self, json):
        result = json['result']
        xbusd = result['XXBTZUSD'] 
        xbusd_a = xbusd['a']
        xbusd_b = xbusd['a']
        xbusd_c = xbusd['c']
        xbusd_v = xbusd['v']
        xbusd_p = xbusd['p']
        xbusd_t = xbusd['t']
        xbusd_l = xbusd['l']
        xbusd_h = xbusd['h']
        xbusd_o = xbusd['o']
        self.timestamp = datetime.now()
        self.ask = xbusd_a[0]
        self.ask_lot = xbusd_a[2]
        self.bid = xbusd_b[0]
        self.bid_lot = xbusd_b[2]
        self.last_closed = xbusd_c[0]
        self.last_closed_lot = xbusd_c[1]
        self.today_volume = xbusd_v[0]
        self.last_day_volume = xbusd_v[1]
        self.weighted_today_volume = xbusd_p[0]
        self.weighted_last_day_volume = xbusd_p[1]
        self.today_trades = xbusd_t[0]
        self.last_day_trades = xbusd_t[1]
        self.today_low = xbusd_l[0]
        self.last_day_low = xbusd_l[1]
        self.today_high = xbusd_h[0]
        self.last_day_high = xbusd_h[1]
        self.open_price = xbusd_o[0]
