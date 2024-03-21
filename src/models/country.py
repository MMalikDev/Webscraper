from dataclasses import dataclass

from sqlalchemy import Column, Float, Integer, String

from database import Base

from ._base import MiscItem


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


@dataclass
class CountryItem(MiscItem):
    name: str
    capital: str
    population: int
    area: float

    def get_id(self):
        return "".join(filter(str.isalnum, self.name)).lower()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
