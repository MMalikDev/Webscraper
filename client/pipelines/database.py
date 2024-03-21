import hashlib
from datetime import datetime

from database import DataAccessLayer
from itemadapter import ItemAdapter
from scrapy import Item, Spider


class DatabasePipeline:
    def open_spider(self, spider: Spider):
        self.db = DataAccessLayer(model=spider.db)

    def process_item(self, item: Item, spider: Spider) -> Item:
        data = ItemAdapter(item).asdict()

        id = data.pop("id", "_blank")
        id_hash = int(hashlib.sha1(id.encode("utf-8")).hexdigest(), 16) % (10**8)

        data["updated_date"] = datetime.now().isoformat()

        if not self.db.update(id_hash, data):
            data["id"] = id_hash
            data["creation_date"] = data["updated_date"]
            self.db.create(data)
        return item
