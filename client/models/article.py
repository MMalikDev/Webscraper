import scrapy
from sqlalchemy import Column, Integer, String

from database import Base


class Article(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    title: str = Column(String, index=True)
    link: str = Column(String)
    description: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class ArticleItem(scrapy.Item):
    id: str = scrapy.Field()
    title: str = scrapy.Field()
    link: str = scrapy.Field()
    description: str = scrapy.Field()
