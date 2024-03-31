import scrapy
from scrapy.http import TextResponse

from configs.schema import schema


class DynamicSpider(scrapy.Spider):
    name = "dynamicSpider"

    def __init__(self):
        super().__init__(
            schema.name,
            start_urls=schema.urls,
            allowed_domains=schema.domains,
        )
        self.db = schema.db
        self.item = schema.item

        self.parent_nodes = schema.parent_nodes
        self.child_nodes = schema.child_nodes
        self.next_node = schema.next_node

    def parse(self, response: TextResponse):
        for quote in response.css(self.parent_nodes):
            item = self.item()
            for k, v in self.child_nodes.items():
                nodes = quote.css(v).getall()
                item[k] = " ".join([i.strip() for i in nodes]).strip()
            yield item

        if not self.next_node:
            return

        if next_url := response.css(self.next_node).extract_first():
            yield scrapy.Request(response.urljoin(next_url))
