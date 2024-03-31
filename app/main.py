from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from configs.core import settings
from lib.utilities import debug


# ---------------------------------------------------------------------- #
# Main Functions                                                         #
# ---------------------------------------------------------------------- #
# @debug
def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(settings.SPIDER)
    process.start()


if __name__ == "__main__":
    main()
