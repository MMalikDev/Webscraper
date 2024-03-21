from collections import namedtuple

from ._base import Miscellaneous, MiscItem
from .article import Article, ArticleItem
from .books import Books, BooksItem
from .country import Country, CountryItem
from .jobs import Jobs, JobsItem
from .links import Links, LinksItem
from .teams import Teams, TeamsItem
from .turtles import Turtles, TurtlesItem

ModelTypes = namedtuple("model_groups", "db, item")

OPTIONS = {
    Miscellaneous.__name__: ModelTypes(Miscellaneous, MiscItem),
    Article.__name__: ModelTypes(Article, ArticleItem),
    Books.__name__: ModelTypes(Books, BooksItem),
    Country.__name__: ModelTypes(Country, CountryItem),
    Jobs.__name__: ModelTypes(Jobs, JobsItem),
    Links.__name__: ModelTypes(Links, LinksItem),
    Teams.__name__: ModelTypes(Teams, TeamsItem),
    Turtles.__name__: ModelTypes(Turtles, TurtlesItem),
}
