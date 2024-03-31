import scrapy
from sqlalchemy import Column, Integer, String

from database import Base


class Books(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    url: str = Column(String)
    img: str = Column(String)
    title: str = Column(String)
    price: str = Column(String)
    availability: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class BooksItem(scrapy.Item):
    id: str = scrapy.Field()
    url: str = scrapy.Field()
    img: str = scrapy.Field()
    title: str = scrapy.Field()
    price: str = scrapy.Field()
    availability: str = scrapy.Field()
