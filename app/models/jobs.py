import scrapy
from sqlalchemy import Column, Integer, String

from database import Base


class Jobs(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    title: str = Column(String)
    company: str = Column(String)
    location: str = Column(String)
    date_posted: str = Column(String)
    link: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class JobsItem(scrapy.Item):
    id: str = scrapy.Field()
    title: str = scrapy.Field()
    company: str = scrapy.Field()
    location: str = scrapy.Field()
    date_posted: str = scrapy.Field()
    link: str = scrapy.Field()
