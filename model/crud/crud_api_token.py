from datetime import datetime

from dateutil.relativedelta import relativedelta
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound, StaleDataError

from db.db_config import SESSION

from ..orm_models import ApiTokenOrm


class CrudApiToken:

    def __init__(self):
        self.session = SESSION

    def _rollback_session(self):
        self.session.rollback()

    def _close_session(self):
        self.session.close()

    def _commit_session(self):
        self.session.commit()

    def select_api_token(self, header):
        try:
            api_token = (
                self.session.query(ApiTokenOrm)
                .filter(
                    ApiTokenOrm.api_key == header["api_key"],
                    ApiTokenOrm.api_secret_key == header["api_secret_key"],
                )
                .one()
            )
        except (NoResultFound, MultipleResultsFound, SQLAlchemyError) as e:
            select_result = e

        else:
            if api_token:
                select_result = True
            else:
                select_result = False

        finally:
            self._close_session()

        return select_result

    def update_api_token(self, token):
        try:
            api_token = (
                self.session.query(ApiTokenOrm)
                .filter(
                    ApiTokenOrm.api_key == token.api_key,
                    ApiTokenOrm.api_secret_key == token.api_secret_key,
                )
                .one()
            )

            api_token.effective_datetime = datetime.now() + relativedelta(years=1)

            self._commit_session()
        except (NoResultFound, MultipleResultsFound) as e:
            update_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            update_result = e

        except SQLAlchemyError as e:
            update_result = e

            if api_token:
                self._rollback_session()

        else:
            update_result = True

        finally:
            self._close_session()

        return update_result
