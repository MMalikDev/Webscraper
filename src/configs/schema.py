import json
from typing import Dict, List, Optional, Union

import models

from .core import settings


class Schema:
    def __init__(self, filepath: str) -> None:
        configs: Dict[str, Union[str, List[str], Dict[str, str]]]
        with open(filepath, "r") as file:
            configs = json.load(file)

        self.js_required: bool = configs.get("js_required", False)
        self.crawl: bool = configs.get("crawl", False)
        self.api: bool = configs.get("api", False)
        self.model: str = configs.get("model")

        model_types = models.OPTIONS.get(self.model)
        self.db = model_types.db
        self.item = model_types.item

        self.key: str = configs.get("key")
        self.name: str = configs.get("name")
        self.headers: str = configs.get("headers")
        self.url: List[Optional[str]] = configs.get("url")

        self.parent_nodes: str = configs.get("parent_nodes")
        self.child_nodes: Dict[str, str] = configs.get("child_nodes")

        self.page: str = configs.get("page", "")
        self.page_min: int = configs.get("page_min", 1)
        self.page_limit: int = configs.get("page_limit", 2)


schema = Schema(settings.WEBSITE_SETTINGS_PATH)
