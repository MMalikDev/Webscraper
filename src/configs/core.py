from lib.utilities import load_bool, load_variable


class Settings:
    DATABASE_URI: str = load_variable("DATABASE_URI", "sqlite+pysqlite:///sqlite.db")
    SHOW_DATA: bool = load_bool("SHOW_DATA") or load_bool("show")
    WEBSITE_SETTINGS_PATH: str = load_variable(
        "WEBSITE_SETTINGS_PATH", "configs/json/countries.json"
    )


settings = Settings()
