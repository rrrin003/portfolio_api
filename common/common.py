"""汎用関数モジュール

汎用関数をまとめたモジュール
"""

from datetime import datetime


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
