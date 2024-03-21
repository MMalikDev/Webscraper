import scrapy
from sqlalchemy import Column, Integer, String

from database import Base


class Quotes(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    author: str = Column(String, index=True)
    quote: str = Column(String)
    tags: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class QuotesItem(scrapy.Item):
    id: str = scrapy.Field()
    author: str = scrapy.Field()
    quote: str = scrapy.Field()
    tags: str = scrapy.Field()
