from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime

from ..db.db_config import SESSION


class Base(object):
    """ベースモデル"""

    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.now, nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, default=datetime.now, onupdate=datetime.now(), nullable=False
        )


Base = declarative_base(cls=Base)
Base.query = SESSION.query_property()
