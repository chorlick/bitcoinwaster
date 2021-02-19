import sqlalchemy
import logging 
from sqlalchemy.orm import sessionmaker
import threading
from sqlalchemy.ext.declarative import declarative_base
import bitcointick
import sys
import sqlalchemy_utils

class BitcoinDb :
    Base = declarative_base()
    metadata =  sqlalchemy.MetaData()
    engine = None
    db_url = "sqlite:///C:\\Users\\chorl\\code\\kraken\\bitcoin.db"
    session = None
    mutex = None
    session_maker = None
    DBSession = None

    def __init__(self) : 
        self.mutex = threading.Lock()

    def start(self) :
        try : 
            if not sqlalchemy_utils.database_exists(self.db_url) : 
                sqlalchemy_utils.create_database(self.db_url)

            logging.info("Starting bitcoin db")
            self.engine = sqlalchemy.create_engine(self.db_url, echo=False)
            self.Base.metadata.bind = self.engine
            self.metadata = self.Base.metadata
            self.DBSession = sessionmaker(bind=self.engine)
            self.session = self.DBSession()
            self.create_data_types()
            logging.getLogger('sqlalchemy').setLevel(logging.ERROR)
            logging.info("Db started successfully")
        except Exception as e : 
            logging.error("Error in starting db : {}".format(e))

    def stop(self) : 
        self.session.close()

    def save(self, obj):
        try : 
            self.mutex.acquire()
            self.session.add(obj)
            self.session.commit()
        except Exception as e: 
            logging.error("Error in saving db object to db : {}".format(e))

        finally : 
            self.mutex.release()
        
    def create_data_types(self) :
        self.mutex.acquire()
        sqlalchemy.Table('bitcoin_tick', self.metadata, 
        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True),
        sqlalchemy.Column('timestamp', sqlalchemy.DateTime),
        sqlalchemy.Column('ask', sqlalchemy.Float),
        sqlalchemy.Column('ask_lot', sqlalchemy.Integer),
        sqlalchemy.Column('bid', sqlalchemy.Float),
        sqlalchemy.Column('bid_lot', sqlalchemy.Integer),
        sqlalchemy.Column('last_closed', sqlalchemy.Float),
        sqlalchemy.Column('last_closed_lot', sqlalchemy.Float),
        sqlalchemy.Column('today_volume', sqlalchemy.Float),
        sqlalchemy.Column('last_day_volume', sqlalchemy.Float),
        sqlalchemy.Column('weighted_today_volume', sqlalchemy.Float),
        sqlalchemy.Column('weighted_last_day_volume', sqlalchemy.Float),   
        sqlalchemy.Column('today_trades', sqlalchemy.Integer),
        sqlalchemy.Column('last_day_trades', sqlalchemy.Integer),
        sqlalchemy.Column('today_low', sqlalchemy.Float),
        sqlalchemy.Column('last_day_low', sqlalchemy.Float),
        sqlalchemy.Column('today_high', sqlalchemy.Float),
        sqlalchemy.Column('last_day_high', sqlalchemy.Float),
        sqlalchemy.Column('open_price', sqlalchemy.Float)
        )
        self.metadata.create_all()
        self.mutex.release()