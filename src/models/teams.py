from dataclasses import dataclass

from sqlalchemy import Column, Float, Integer, String

from database import Base

from ._base import MiscItem


class Teams(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    name: str = Column(String)
    year: int = Column(Integer, index=True)
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


@dataclass
class TeamsItem(MiscItem):
    name: str
    year: int
    wins: int
    losses: int
    ot_losses: int
    pct: float
    gf: int
    ga: int
    diff: int

    def get_id(self):
        return "".join(filter(str.isalnum, f"{self.name}{self.year}")).lower()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
