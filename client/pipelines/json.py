# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

from itemadapter import ItemAdapter
from scrapy import Item, Spider


class JsonPipeline:
    def open_spider(self, spider: Spider):
        self.data = []

        file = "data/%s.json" % spider.name
        self.file = open(file, "w")

    def close_spider(self, spider: Spider):
        content = json.dumps(self.data, indent=2)
        self.file.write(content)
        self.file.close()

    def process_item(self, item: Item, spider: Spider) -> Item:
        data = ItemAdapter(item).asdict()
        self.data.append(data)
        return item
