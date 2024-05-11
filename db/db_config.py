"""database設定モジュール

database、sessionの生成をまとめたモジュール
"""

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# DBのパス
DATABASE = "sqlite:///db/database/portfolio_db.sqlite3"

# ENGINE（DB接続オブジェクト）の作成
ENGINE = create_engine(DATABASE, echo=False)

# SESSIONの作成
SESSION = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

# メタデータオブジェクトを作成
METADATA = MetaData()
