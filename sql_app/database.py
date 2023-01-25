from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#CONNECTION_STRING = f'mariadb+mariadbconnector://root:mypass@127.0.0.1:3306/api_data'
CONNECTION_STRING = f'mariadb+mariadbconnector://root:{os.getenv("DB_PASS")}@127.0.0.1:3306/api_data'

engine = create_engine(CONNECTION_STRING)

# a bit of a hack, proper setup of database should be done elsewhere
#if ('api_data',) not in engine.execute('show_schemas').all():
#    engine.execute(sqlalchemy.schema.CreateSchema('api_data'))

my_sessionmaker = sessionmaker(bind=engine, autocommit=False, autoflush=False)

base = declarative_base()
