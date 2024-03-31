import scrapy
from sqlalchemy import Column, Float, Integer, String

from database import Base


class Teams(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    name: str = Column(String)
    year: int = Column(Integer)
    wins: int = Column(Integer)
    losses: int = Column(Integer)
    ot_losses: int = Column(Integer)
    pct: float = Column(Float)
    gf: int = Column(Integer)
    ga: int = Column(Integer)
    diff: int = Column(Integer)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class TeamsItem(scrapy.Item):
    id: str = scrapy.Field()
    name: str = scrapy.Field()
    year: int = scrapy.Field(serializer=int)
    wins: int = scrapy.Field(serializer=int)
    losses: int = scrapy.Field(serializer=int)
    ot_losses: int = scrapy.Field(serializer=int)
    pct: float = scrapy.Field(serializer=float)
    gf: int = scrapy.Field(serializer=int)
    ga: int = scrapy.Field(serializer=int)
    diff: int = scrapy.Field(serializer=int)
