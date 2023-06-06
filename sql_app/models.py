from sqlalchemy import Column, DateTime, Integer, String

from sql_app.database import base


class UrlData(base):
    __tablename__ = "url_data"
    id = Column(Integer, primary_key=True)
    long_url = Column(String(length=200))
    short_url = Column(String(length=200))
    created = Column(DateTime)
    klicks = Column(Integer)
    description = Column(String(length=1000))
