import scrapy
from sqlalchemy import Column, Integer, String

from database import Base


class Miscellaneous(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    value: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class MiscItem(scrapy.Item):
    id: str = scrapy.Field()
    value: str = scrapy.Field()
