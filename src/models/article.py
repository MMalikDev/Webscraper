from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from database import Base

from ._base import MiscItem


class Article(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    title: str = Column(String, index=True)
    link: str = Column(String)
    description: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


@dataclass
class ArticleItem(MiscItem):
    title: str
    link: str
    description: str

    def get_id(self) -> int:
        return "".join(filter(str.isalnum, self.title)).lower()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id})"
