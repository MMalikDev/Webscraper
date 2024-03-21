import scrapy
from sqlalchemy import Column, Float, Integer, String

from database import Base


class Country(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    name: str = Column(String)
    capital: str = Column(String)
    population: int = Column(Integer)
    area: float = Column(Float)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class CountryItem(scrapy.Item):
    id: str = scrapy.Field()
    name: str = scrapy.Field()
    capital: str = scrapy.Field()
    population: int = scrapy.Field(serializer=int)
    area: float = scrapy.Field(serializer=float)
