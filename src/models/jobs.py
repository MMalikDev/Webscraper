from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from database import Base

from ._base import MiscItem


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


@dataclass
class JobsItem(MiscItem):

    title: str
    company: str
    location: str
    date_posted: str
    link: str

    def get_id(self):
        return "".join(filter(str.isalnum, f"{self.title} {self.company}")).lower()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
