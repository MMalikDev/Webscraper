from lib.utilities import load_variable


class Settings:
    DATABASE_URI: str = load_variable("DATABASE_URI", "sqlite+pysqlite:///sqlite.db")
    SPIDER: str = load_variable("SPIDER", "dynamicSpider")
    WEBSITE_SETTINGS_PATH: str = load_variable(
        "WEBSITE_SETTINGS_PATH",
        "configs/json/quotes.json",
    )


settings = Settings()
