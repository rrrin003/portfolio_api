"""汎用関数モジュール

汎用関数をまとめたモジュール
"""

import hashlib
import secrets

from http import HTTPStatus
from datetime import datetime

from fastapi.responses import JSONResponse
from sqlalchemy.exc import DataError, IntegrityError, SQLAlchemyError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound, StaleDataError

from common import constants


def get_datetime_str(format):
    """日時文字列取得関数

    Args:
        format (string): 取得したい日時のフォーマット文字列

    Returns:
        string: formatで指定した形式の日時文字列

    Examples:
        get_datetime_str("%Y-%m-%d")
    """

    return datetime.now().date().strftime(format)


def check_existence_of_token(header):
    if "api_key" in header and "api_secret_key" in header:
        result = True
    else:
        result = JSONResponse(
            content={"message": constants.API_TOKEN_ERROR_MESSAGE},
            status_code=HTTPStatus.UNAUTHORIZED,
        )

    return result


def hash_password(password, salt_length=32, hash_algorithm="sha256"):
    salt = secrets.token_bytes(salt_length)
    salt_hex = salt.hex()
    salted_password = salt + password.encode("utf-8")
    hashed_password = hashlib.new(hash_algorithm, salted_password).hexdigest()

    return {"hashed_password": hashed_password, "salt": salt_hex}


def verify_password(plain_password, salt_hex, hashed_password, hash_algorithm="sha256"):
    """パスワードの検証

    Args:
        plain_password (str): 検証対象の平文パスワード
        salt_hex (str): 16進数表記のソルト文字列
        hashed_password (str): ハッシュ化されたパスワード
        hash_algorithm (str, optional): ハッシュアルゴリズムの指定。デフォルトは "sha256"。

    Returns:
        bool: パスワードが正しい場合はTrue、そうでない場合はFalse。
    """

    salt = bytes.fromhex(salt_hex)
    salted_password = salt + plain_password.encode("utf-8")
    calculated_hash = hashlib.new(hash_algorithm, salted_password).hexdigest()

    return calculated_hash == hashed_password


def convert_orm_list_to_dict(orm_list):
    """ORMリストから辞書リストへ変換

    Args:
        orm_list: SQLAlchemy ORMリスト

    Returns:
        result_list: カラム名をキーにした辞書が格納されたリスト
    """

    if not orm_list:
        return []

    column_names = orm_list[0].__table__.columns.keys()
    dict_list = []

    for orm_obj in orm_list:
        obj_dict = {column: getattr(orm_obj, column) for column in column_names}
        dict_list.append(obj_dict)

    return dict_list


def convert_orm_object_to_dict(orm_object):
    """ORMオブジェクトから辞書型へ変換

    Args:
        orm_object: SQLAlchemy ORMオブジェクト

    Returns:
        orm_dict: カラム名をキーにした辞書
    """
    orm_dict = {
        column.key: getattr(orm_object, column.key)
        for column in orm_object.__table__.columns
    }

    return orm_dict


def check_crud_result(excption):
    """CRUDの結果を判定

    Args:
        excption (object): CRUD処理の結果

    Returns:
        result: 例外オブジェクト or True
    """

    if isinstance(excption, DataError):
        result = JSONResponse(content={"message": str(excption)}, status_code=400)
    elif isinstance(excption, NoResultFound):
        result = JSONResponse(content={"message": str(excption)}, status_code=404)
    elif isinstance(excption, StaleDataError):
        result = JSONResponse(content={"message": str(excption)}, status_code=409)
    elif isinstance(excption, IntegrityError):
        result = JSONResponse(content={"message": str(excption)}, status_code=409)
    elif isinstance(excption, MultipleResultsFound):
        result = JSONResponse(content={"message": str(excption)}, status_code=500)
    elif isinstance(excption, SQLAlchemyError):
        result = JSONResponse(content={"message": str(excption)}, status_code=500)
    elif isinstance(excption, BaseException):
        result = JSONResponse(content={"message": str(excption)}, status_code=500)
    else:
        result = True
    return result
