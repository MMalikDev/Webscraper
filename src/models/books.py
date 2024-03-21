from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from database import Base

from ._base import MiscItem


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


@dataclass
class BooksItem(MiscItem):
    url: str
    img: str
    title: str
    price: str
    availability: str

    def get_id(self):
        return "".join(filter(str.isalnum, self.title)).lower()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
