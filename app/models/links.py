import scrapy
from sqlalchemy import Column, Integer, String

from database import Base


class Links(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    name: str = Column(String)
    url: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class LinksItem(scrapy.Item):
    id: str = scrapy.Field()
    name: str = scrapy.Field()
    url: str = scrapy.Field()
