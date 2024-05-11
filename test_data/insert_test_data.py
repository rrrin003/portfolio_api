from db.db_config import SESSION
from test_data.data import test_data


def insert_api_token():
    SESSION.add_all([test_data.api_token])
    SESSION.commit()
    SESSION.close()


def insert_works_data():
    SESSION.add_all([test_data.works1, test_data.works2, test_data.works3])
    SESSION.commit()
    SESSION.close()


def insert_blog_data():
    SESSION.add_all([test_data.blog1, test_data.blog2, test_data.blog3])
    SESSION.commit()
    SESSION.close()


def insert_contact_data():
    SESSION.add_all([test_data.contact1, test_data.contact2, test_data.contact3])
    SESSION.commit()
    SESSION.close()


def insert_user_data():
    SESSION.add_all([test_data.user1, test_data.user2, test_data.user3])
    SESSION.commit()
    SESSION.close()
