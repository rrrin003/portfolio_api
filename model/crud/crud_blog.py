from sqlalchemy.exc import DataError, IntegrityError, SQLAlchemyError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound, StaleDataError

from db.db_config import SESSION

from ..orm_models import BlogOrm


class CrudBlog:
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

    def select_all_blog(self):
        try:
            blog = self.session.query(BlogOrm).all()

        except SQLAlchemyError as e:
            select_result = e

        else:
            select_result = blog

        finally:
            self._close_session()

            return select_result

    def insert_blog(self, request_body):
        blog = BlogOrm()

        blog.title = request_body.title
        blog.body = request_body.body
        blog.photo = request_body.photo
        blog.tag = request_body.tag
        blog.draft_flg = request_body.draft_flg
        blog.hidden_flg = request_body.hidden_flg

        try:
            self._add_session(blog)
            self._commit_session()

        except (IntegrityError, DataError, SQLAlchemyError) as e:
            self._rollback_session()

            insert_result = e

        else:
            insert_result = True

        finally:
            self._close_session()

            return insert_result

    def select_blog_by_id(self, path_param):
        try:
            blog = self.session.query(BlogOrm).filter(BlogOrm.id == path_param).one()

        except (NoResultFound, MultipleResultsFound, SQLAlchemyError) as e:
            get_result = e

        else:
            get_result = blog

        finally:
            self._close_session()

            return get_result

    def update_blog_by_id(self, path_param, request_body):

        try:
            blog = self.session.query(BlogOrm).filter(BlogOrm.id == path_param).one()

            blog.title = request_body.title
            blog.body = request_body.body
            blog.photo = request_body.photo
            blog.tag = request_body.tag
            blog.draft_flg = request_body.draft_flg
            blog.hidden_flg = request_body.hidden_flg
            blog.delete_flg = request_body.delete_flg

            self._commit_session()

        except (NoResultFound, MultipleResultsFound) as e:
            put_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            put_result = e

        except SQLAlchemyError as e:
            put_result = e

            if blog:
                self._rollback_session()

        else:
            put_result = True

        finally:
            self._close_session()

            return put_result

    def delete_blog_by_id(self, path_param):
        try:
            blog = self.session.query(BlogOrm).filter(BlogOrm.id == path_param).one()

            self._delete_session(blog)
            self._commit_session()

        except (NoResultFound, MultipleResultsFound) as e:
            delete_result = e

        except (IntegrityError, StaleDataError) as e:
            self._rollback_session()

            delete_result = e

        except SQLAlchemyError as e:
            delete_result = e

            if blog:
                self._rollback_session()

        else:
            delete_result = True

        finally:
            self._close_session()

            return delete_result
