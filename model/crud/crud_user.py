from sqlalchemy.exc import DataError, IntegrityError, SQLAlchemyError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound, StaleDataError

from db.db_config import SESSION

from ..orm_models import UserOrm


class CrudUser:
    def __init__(self) -> None:
        self.session = SESSION

    def _add_session(self, instance):
        self.session.add(instance)

    def _delete_session(self, instance):
        self.session.delete(instance)

    def _rollback_session(self):
        self.session.rollback()

    def _close_session(self):
        self.session.close()

    def _commit_session(self):
        self.session.commit()

    def select_all_user(self):
        try:
            user = self.session.query(UserOrm).all()

        except SQLAlchemyError as e:
            get_result = e

        else:
            get_result = user

        finally:
            self._close_session()

            return get_result

    def insert_user(self, request_body):

        user = UserOrm()

        user.name = request_body.name
        user.email = request_body.email
        user.password = request_body.password["hashed_password"]
        user.salt = request_body.password["salt"]

        try:
            self._add_session(user)
            self._commit_session()

        except (IntegrityError, DataError, SQLAlchemyError) as e:
            self._rollback_session()

            post_result = e

        else:
            post_result = True

        finally:
            self._close_session()

            return post_result

    def select_user_by_id(self, path_param):
        try:
            user = self.session.query(UserOrm).filter(UserOrm.id == path_param).one()

        except (NoResultFound, MultipleResultsFound, SQLAlchemyError) as e:
            get_result = e

        else:
            get_result = user

        finally:
            self._close_session()

            return get_result

    def select_user_by_email(self, request_body):
        try:
            user = (
                self.session.query(UserOrm)
                .filter(UserOrm.email == request_body.email)
                .one()
            )

        except (NoResultFound, MultipleResultsFound, SQLAlchemyError) as e:
            get_result = e

        else:
            get_result = user

        finally:
            self._close_session()

            return get_result

    def update_user_by_id(self, path_param, request_body):
        try:
            user = self.session.query(UserOrm).filter(UserOrm.id == path_param).one()

            user.name = request_body.name
            user.email = request_body.email
            user.password = request_body.password["hashed_password"]
            user.salt = request_body.password["salt"]
            user.delete_flg = request_body.delete_flg

            self._commit_session()

        except (NoResultFound, MultipleResultsFound) as e:
            put_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            put_result = e

        except SQLAlchemyError as e:
            put_result = e

            if user:
                self._rollback_session()

        else:
            put_result = True

        finally:
            self._close_session()

            return put_result

    def delete_user_by_id(self, path_param):
        try:
            user = self.session.query(UserOrm).filter(UserOrm.id == path_param).one()

            self._delete_session(user)
            self._commit_session()

        except (NoResultFound, MultipleResultsFound) as e:
            delete_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            delete_result = e

        except SQLAlchemyError as e:
            delete_result = e

            if user:
                self._rollback_session()

        else:
            delete_result = True

        finally:
            self._close_session()

            return delete_result
