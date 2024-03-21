# WebScraper

## Overview

This repository contains two web scraping setups, each capable of operating both locally and within a Docker container.
Choose between the following options:

- **Scapy Framework**: Leveraging a dynamic spider powered by JSON configurations for traversing the web. Visit [Scrapy's official documentation](https://docs.scrapy.org/en/latest/) to learn more.

- **Requests & Webdriver with HTML Parser**: An alternative and simpler approach for acquiring HTML content through HTTPX or Playwright and storing it locally for future use. Subsequently parse the webpages utilizing Selectolax, saving the extracted information into a database as well as local JSON files.

> Keep your CSS selectors stored in the JSON file, enabling seamless incorporation of new elements into your database via simple addition of item models.

### Data Persistence

Persist gathered data in an SQL database of your choice. Included are connection strings (i.e. URIs) for PostgreSQL and SQLite databases. As a value-added feature, this setup includes a reverse proxy to manage the pgAdmin4 dashboard!

> Note: In order to identify records inside the database, utilize the SHA1 hash derived from a designated field.

## Getting Started

Initiate by setting up one of the required dependencies below:

- Python 3.x
- Docker

Subsequent actions include:

1. Clone this repository.
1. Generate a **`.env`** file from the provided **'`.env.example`'**.

Additional guidance and support can be accessed via:

```bash
bash run.sh -h
```

## Recommended Websites for Practicing

- [HTTP Bin](https://Httpbin.org)
- [Crawler Test](https://crawler-test.com)
- [Scrape This Site](https://scrapethissite.com)
- [The Internet](https://the-internet.herokuapp.com)
- [Fake Jobs Site](https://realpython.github.io/fake-jobs)
- [To Scrape](https://toscrape.com) :
  - [Books](https://books.toscrape.com)
  - [Quotes](https://quotes.toscrape.com)
