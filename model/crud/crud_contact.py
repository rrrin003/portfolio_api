from sqlalchemy.exc import DataError, IntegrityError, SQLAlchemyError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound, StaleDataError

from db.db_config import SESSION

from ..orm_models import ContactOrm


class CrudContact:
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

    def select_all_contact(self):
        try:
            contact = self.session.query(ContactOrm).all()

        except SQLAlchemyError as e:
            select_result = e

        else:
            select_result = contact

        finally:
            self._close_session()

            return select_result

    def insert_contact(self, request_body):
        contact = ContactOrm()

        contact.title = request_body.title
        contact.name = request_body.name
        contact.company_name = request_body.company_name
        contact.email = request_body.email
        contact.phone_number = request_body.phone_number
        contact.body = request_body.body

        try:
            self._add_session(contact)
            self._commit_session()

        except (IntegrityError, DataError, SQLAlchemyError) as e:
            self._rollback_session()

            insert_result = e

        else:
            insert_result = True

        finally:
            self._close_session()

            return insert_result

    def select_contact_by_id(self, path_param):
        try:
            contact = (
                self.session.query(ContactOrm).filter(ContactOrm.id == path_param).one()
            )

        except (NoResultFound, MultipleResultsFound, SQLAlchemyError) as e:
            select_result = e

        else:
            select_result = contact

        finally:
            self._close_session()

            return select_result

    def update_contact_by_id(self, path_param, request_body):
        try:
            contact = (
                self.session.query(ContactOrm).filter(ContactOrm.id == path_param).one()
            )

            contact.delete_flg = request_body.delete_flg

            self._commit_session()

        except (NoResultFound, MultipleResultsFound) as e:
            update_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            update_result = e

        except SQLAlchemyError as e:
            update_result = e

            if contact:
                self._rollback_session()

        else:
            update_result = True

        finally:
            self._close_session()

            return update_result

    def delete_contact_by_id(self, path_param):
        try:
            contact = (
                self.session.query(ContactOrm).filter(ContactOrm.id == path_param).one()
            )

            self._delete_session(contact)
            self._commit_session()

        except (NoResultFound, MultipleResultsFound) as e:
            delete_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            delete_result = e

        except SQLAlchemyError as e:
            delete_result = e

            if contact:
                self._rollback_session()

        else:
            delete_result = True

        finally:
            self._close_session()

            return delete_result
