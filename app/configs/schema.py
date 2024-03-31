import json
from typing import Dict, List, Optional, Union

import models

from .core import settings


class Schema:
    def __init__(self, filepath: str) -> None:
        configs: Dict[str, Union[str, List[str], Dict[str, str]]]
        with open(filepath, "r") as file:
            configs = json.load(file)

        model: str = configs.get("model")
        model_types = models.OPTIONS.get(model)
        self.db = model_types.db
        self.item = model_types.item

        self.name: str = configs.get("name")
        self.urls: List[Optional[str]] = configs.get("urls")
        self.domains: List[Optional[str]] = configs.get("domains")

        self.parent_nodes: str = configs.get("parent_nodes")
        self.child_nodes: Dict[str, str] = configs.get("child_nodes")
        self.next_node: Optional[str] = configs.get("next_node")


schema = Schema(settings.WEBSITE_SETTINGS_PATH)
