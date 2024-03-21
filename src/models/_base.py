from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String

from database import Base


class Miscellaneous(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    value: str = Column(String)

    updated_date: str = Column(String)
    creation_date: str = Column(String)

    def __repr__(self) -> str:
        return "Hash(%i)" % self.id


class MiscItem:
    value: str

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.id: str = self.get_id()
        self.updated_date: str = datetime.now().isoformat()

    def __post_init__(self) -> None:
        self.id: str = self.get_id()
        self.updated_date: str = datetime.now().isoformat()

    def get_id(self) -> int:
        return self.value or uuid4().hex

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id})"
