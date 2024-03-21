from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from database import Base

from ._base import MiscItem


class Turtles(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    name: str = Column(String)
    img: str = Column(String)
    link: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


@dataclass
class TurtlesItem(MiscItem):
    name: str
    img: str
    link: str

    def get_id(self):
        return "".join(filter(str.isalnum, self.name)).lower()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
