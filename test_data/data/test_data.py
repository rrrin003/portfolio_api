from datetime import datetime

from dateutil.relativedelta import relativedelta

from model.orm_models import ApiTokenOrm, BlogOrm, ContactOrm, UserOrm, WorksOrm

now_date_time = datetime.now()
plus1_date_time = now_date_time + relativedelta(years=1)

api_token = ApiTokenOrm(
    api_key="eee86b6b-5369-4f3d-b336-33732b0e416b",
    api_secret_key="c7fbec71-ce9d-4f9f-9d5d-28f1131ad85a",
    datetime_of_issue=now_date_time.strftime("%Y-%m-%d-%H-%M"),
    effective_datetime=plus1_date_time.strftime("%Y-%m-%d-%H-%M"),
)
works1 = WorksOrm(
    title="ワークスタイトル01",
    body="ワークス本文01",
    photo="{'main': '/img/works/test00.jpg'}",
    tag="{'1': 'tag01'}",
    draft_flg=False,
    hidden_flg=False,
)
works2 = WorksOrm(
    title="ワークスタイトル02",
    body="ワークス本文02",
    photo="{'main': '/img/works/test00.jpg'}",
    tag="{'1': 'tag01','2': 'tag02'}",
    draft_flg=False,
    hidden_flg=False,
)
works3 = WorksOrm(
    title="ワークスタイトル03",
    draft_flg=False,
    hidden_flg=False,
)

blog1 = BlogOrm(
    title="ブログタイトル01",
    body="ブログ本文01",
    photo="{'main': '/img/blog/test00.jpg'}",
    tag="{'1': 'tag01'}",
    draft_flg=False,
    hidden_flg=False,
)
blog2 = BlogOrm(
    title="ブログタイトル02",
    body="ブログ本文02",
    photo="{'main': '/img/blog/test00.jpg'}",
    tag="{'1': 'tag01','2': 'tag02'}",
    draft_flg=False,
    hidden_flg=False,
)
blog3 = BlogOrm(
    title="ブログタイトル03",
    draft_flg=False,
    hidden_flg=False,
)

contact1 = ContactOrm(
    title="コンタクトタイトル01",
    name="コンタクト太郎",
    company_name="株式会社コンタクト01",
    email="contact01@example.com",
    phone_number="00011112222",
    body="コンタクト本文01",
)
contact2 = ContactOrm(
    title="コンタクトタイトル02",
    name="コンタクト花子",
    company_name="株式会社コンタクト02",
    email="contact02@example.com",
    phone_number="33344445555",
    body="コンタクト本文02",
)
contact3 = ContactOrm(
    title="コンタクトタイトル03",
    name="山田コンタクト",
    email="contact03@example.com",
    phone_number="66677778888",
    body="コンタクト本文03",
)

user1 = UserOrm(
    name="山田太郎",
    email="user01@example.com",
    password="password01",
    salt="9b217e06489cd2d7b0b511cf3bbdc438fcec11f45387999106504c4ca95ea6a1",
)
user2 = UserOrm(
    name="鈴木花子",
    email="user02@example.com",
    password="password03",
    salt="9b217e06489cd2d7b0b511cf3bbdc438fcec11f45387999106504c4ca95ea6a1",
)
user3 = UserOrm(
    name="佐藤たかし",
    email="user03@example.com",
    password="password03",
    salt="9b217e06489cd2d7b0b511cf3bbdc438fcec11f45387999106504c4ca95ea6a1",
)
