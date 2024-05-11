from sqlalchemy.exc import DataError, IntegrityError, SQLAlchemyError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound, StaleDataError

from db.db_config import SESSION

from ..orm_models import WorksOrm


class CrudWorks:
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

    def select_all_works(self):
        try:
            works = self.session.query(WorksOrm).all()

        except SQLAlchemyError as e:
            select_result = e

        else:
            select_result = works

        finally:
            self._close_session()

        return select_result

    def insert_works(self, request_body):
        works = WorksOrm()

        works.title = request_body.title
        works.body = request_body.body
        works.photo = request_body.photo
        works.tag = request_body.tag
        works.draft_flg = request_body.draft_flg
        works.hidden_flg = request_body.hidden_flg

        try:
            self._add_session(works)
            self._commit_session()

        except (IntegrityError, DataError, SQLAlchemyError) as e:
            self._rollback_session()

            insert_result = e

        else:
            insert_result = True

        finally:
            self._close_session()

        return insert_result

    def select_works_by_id(self, path_param):
        try:
            works = self.session.query(WorksOrm).filter(WorksOrm.id == path_param).one()

        except (NoResultFound, MultipleResultsFound, SQLAlchemyError) as e:
            select_result = e

        else:
            select_result = works

        finally:
            self._close_session()

        return select_result

    def update_works_by_id(self, path_param, request_body):
        try:
            works = self.session.query(WorksOrm).filter(WorksOrm.id == path_param).one()

            works.title = request_body.title
            works.body = request_body.body
            works.photo = request_body.photo
            works.tag = request_body.tag
            works.draft_flg = request_body.draft_flg
            works.hidden_flg = request_body.hidden_flg
            works.delete_flg = request_body.delete_flg

            self._commit_session()

        except (NoResultFound, MultipleResultsFound) as e:
            update_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            update_result = e

        except SQLAlchemyError as e:
            update_result = e

            if works:
                self._rollback_session()

        else:
            update_result = True

        finally:
            self._close_session()

        return update_result

    def delete_works_by_id(self, path_param):

        try:
            works = self.session.query(WorksOrm).filter(WorksOrm.id == path_param).one()

            self._delete_session(works)
            self._commit_session()

        except (NoResultFound, MultipleResultsFound) as e:
            delete_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            delete_result = e

        except SQLAlchemyError as e:
            delete_result = e

            if works:
                self._rollback_session()

        else:
            delete_result = True

        finally:
            self._close_session()

        return delete_result
