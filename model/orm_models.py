from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, Integer, String, Text

from db.db_config import ENGINE, SESSION


class OrmBase(object):
    """ベースモデル"""

    @declared_attr
    def created_at(cls):
        return Column(
            String(20),
            default=datetime.now().strftime("%Y-%m-%d-%H-%M"),
            nullable=False,
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            String(20),
            default=datetime.now().strftime("%Y-%m-%d-%H-%M"),
            onupdate=datetime.now().strftime("%Y-%m-%d-%H-%M"),
            nullable=False,
        )


OrmBase = declarative_base(cls=OrmBase)
OrmBase.query = SESSION.query_property()


class ApiTokenOrm(OrmBase):
    __tablename__ = "api_tokens"

    api_key = Column(String(50), primary_key=True, unique=True)
    api_secret_key = Column(String(50), nullable=False)
    datetime_of_issue = Column(String(20), nullable=False)
    effective_datetime = Column(String(20), nullable=False)
    delete_flg = Column(Boolean, nullable=False, default=False)


class WorksOrm(OrmBase):
    __tablename__ = "works"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    body = Column(String(200), nullable=True)
    photo = Column(Text, nullable=True)
    tag = Column(Text, nullable=True)
    draft_flg = Column(Boolean, nullable=False, default=True)
    hidden_flg = Column(Boolean, nullable=False, default=True)
    delete_flg = Column(Boolean, nullable=False, default=False)


class BlogOrm(OrmBase):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=True)
    photo = Column(Text, nullable=True)
    tag = Column(Text, nullable=True)
    draft_flg = Column(Boolean, nullable=False, default=True)
    hidden_flg = Column(Boolean, nullable=False, default=True)
    delete_flg = Column(Boolean, nullable=False, default=False)


class ContactOrm(OrmBase):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    name = Column(String(60), nullable=False)
    company_name = Column(String(140), nullable=True)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(25), nullable=False)
    body = Column(Text, nullable=False)
    delete_flg = Column(Boolean, nullable=False, default=False)


class UserOrm(OrmBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    salt = Column(String(64), nullable=False)
    delete_flg = Column(Boolean, nullable=False, default=False)


# デバッグ用のテーブルドロップ命令
OrmBase.metadata.drop_all(bind=ENGINE)

# テーブル生成
OrmBase.metadata.create_all(bind=ENGINE)
