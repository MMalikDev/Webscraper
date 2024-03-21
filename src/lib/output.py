import hashlib
import json
from pathlib import Path
from typing import Dict, List, Union

from database import Base, DataAccessLayer

Data = Dict[str, Union[int, str]]


def save_file(filename: str, data: str) -> None:
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(data)


def save_json(name: str, content: List[Data]) -> None:
    filepath = Path(f"data/json/{name}.json")
    data = json.dumps(content, indent=2)
    save_file(filepath, data)


def save_db(model: Base, items: List[Data]) -> None:
    db = DataAccessLayer(model=model)
    for item in items:
        id = item.pop("id")
        id_hash = int(hashlib.sha1(id.encode("utf-8")).hexdigest(), 16) % (10**8)

        if not db.update(id_hash, item):
            item["id"] = id_hash
            item["creation_date"] = item["updated_date"]
            db.create(item)
