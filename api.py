import logging
from http import HTTPStatus

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from common import constants
from common.common import (
    check_crud_result,
    convert_orm_list_to_dict,
    convert_orm_object_to_dict,
    verify_password,
    check_existence_of_token,
)
from initialize import initialize
from model.classes.blog import Blog
from model.classes.contact import Contact
from model.classes.login import Login
from model.classes.user import User
from model.classes.works import Works
from model.crud.crud_api_token import CrudApiToken
from model.crud.crud_blog import CrudBlog
from model.crud.crud_contact import CrudContact
from model.crud.crud_user import CrudUser
from model.crud.crud_works import CrudWorks
from test_data.insert_test_data import (
    insert_api_token,
    insert_blog_data,
    insert_contact_data,
    insert_user_data,
    insert_works_data,
)

app = FastAPI()

crud_api_token = CrudApiToken()
crud_works = CrudWorks()
crud_blog = CrudBlog()
crud_contact = CrudContact()
crud_user = CrudUser()

initialize()

logger = logging.getLogger(constants.API_LOGGER)


def checkToken(request_header):
    header = dict(request_header)

    check_token = check_existence_of_token(header)

    if check_token is not True:
        return check_token

    crud_result = crud_api_token.select_api_token(header)

    if crud_result is True:
        result = True
    else:
        result = JSONResponse(
            content={"message": constants.API_TOKEN_ERROR_MESSAGE},
            status_code=HTTPStatus.UNAUTHORIZED,
        )

    return result


@app.get("/works")
def get_works(request: Request):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_works.select_all_works()
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_list_to_dict(crud_result)

        return JSONResponse(content=result, status_code=HTTPStatus.OK)
    else:
        return checked_result


@app.post("/works")
def post_works(request: Request, body: Works):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    request_body = body

    crud_result = crud_works.insert_works(request_body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return JSONResponse(content={}, status_code=HTTPStatus.CREATED)
    else:
        return checked_result


@app.get("/works/{id}")
def get_works_by_id(request: Request, id: int):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_works.select_works_by_id(id)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_object_to_dict(crud_result)

        return JSONResponse(content=result, status_code=HTTPStatus.OK)
    else:
        return checked_result


@app.put("/works/{id}")
def put_works(request: Request, id: int, body: Works):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    request_body = body

    crud_result = crud_works.update_works_by_id(id, request_body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return Response(status_code=HTTPStatus.NO_CONTENT)
    else:
        return checked_result


@app.delete("/works/{id}")
def delete_works(request: Request, id: int):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_works.delete_works_by_id(id)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return Response(status_code=HTTPStatus.NO_CONTENT)
    else:
        return checked_result


@app.get("/blog")
def get_blog(request: Request):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_blog.select_all_blog()
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_list_to_dict(crud_result)

        return JSONResponse(content=result, status_code=HTTPStatus.OK)
    else:
        return checked_result


@app.post("/blog")
def post_blog(request: Request, body: Blog):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    request_body = body

    crud_result = crud_blog.insert_blog(request_body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return JSONResponse(content={}, status_code=HTTPStatus.CREATED)
    else:
        return checked_result


@app.get("/blog/{id}")
def get_blog_by_id(request: Request, id: int):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_blog.select_blog_by_id(id)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_object_to_dict(crud_result)

        return JSONResponse(content=result, status_code=HTTPStatus.OK)
    else:
        return checked_result


@app.put("/blog/{id}")
def put_blog(request: Request, id: int, body: Blog):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    request_body = body

    crud_result = crud_blog.update_blog_by_id(id, request_body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return Response(status_code=HTTPStatus.NO_CONTENT)
    else:
        return checked_result


@app.delete("/blog/{id}")
def delete_blog(request: Request, id: int):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_blog.delete_blog_by_id(id)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return Response(status_code=HTTPStatus.NO_CONTENT)
    else:
        return checked_result


@app.get("/contact")
def get_contact(request: Request):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_contact.select_all_contact()
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_list_to_dict(crud_result)

        return JSONResponse(content=result, status_code=HTTPStatus.OK)
    else:
        return checked_result


@app.post("/contact")
def post_contact(request: Request, body: Contact):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    request_body = body

    crud_result = crud_contact.insert_contact(request_body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return JSONResponse(content={}, status_code=HTTPStatus.CREATED)
    else:
        return checked_result


@app.get("/contact/{id}")
def get_contact_by_id(request: Request, id: int):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_contact.select_contact_by_id(id)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_object_to_dict(crud_result)

        return JSONResponse(content=result, status_code=HTTPStatus.OK)
    else:
        return checked_result


@app.put("/contact/{id}")
def put_contact(request: Request, id: int, body: Contact):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    request_body = body

    crud_result = crud_contact.update_contact_by_id(id, request_body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return Response(status_code=HTTPStatus.NO_CONTENT)
    else:
        return checked_result


@app.delete("/contact/{id}")
def delete_contact(request: Request, id: int):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_contact.delete_contact_by_id(id)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return Response(status_code=HTTPStatus.NO_CONTENT)
    else:
        return checked_result


@app.get("/user")
def get_user(request: Request):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_user.select_all_user()
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_list_to_dict(crud_result)

        return JSONResponse(content=result, status_code=HTTPStatus.OK)
    else:
        return checked_result


@app.post("/user")
def post_user(request: Request, body: User):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    request_body = body

    crud_result = crud_user.insert_user(request_body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return JSONResponse(content={}, status_code=HTTPStatus.CREATED)
    else:
        return checked_result


@app.get("/user/{id}")
def get_user_by_id(request: Request, id: int):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_user.select_user_by_id(id)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_object_to_dict(crud_result)

        return JSONResponse(content=result, status_code=HTTPStatus.OK)
    else:
        return checked_result


@app.put("/user/{id}")
def put_user(request: Request, id: int, body: User):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    request_body = body

    crud_result = crud_user.update_user_by_id(id, request_body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return Response(status_code=HTTPStatus.NO_CONTENT)
    else:
        return checked_result


@app.delete("/user/{id}")
def delete_user(request: Request, id: int):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_user.delete_user_by_id(id)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        return Response(status_code=HTTPStatus.NO_CONTENT)
    else:
        return checked_result


@app.post("/login")
def login(request: Request, body: Login):
    check_token_result = checkToken(request.headers)

    if check_token_result is not True:
        return check_token_result

    crud_result = crud_user.select_user_by_email(body)
    checked_result = check_crud_result(crud_result)

    if checked_result is True:
        result = convert_orm_object_to_dict(crud_result)

        print(result)

        password_check = verify_password(
            body.password.get_secret_value(),
            result["salt"],
            result["password"],
        )

        if password_check is True:
            return JSONResponse(content=result, status_code=HTTPStatus.OK)
        else:
            result = {"message": "Password is incorrect."}
            return JSONResponse(content=result, status_code=HTTPStatus.UNAUTHORIZED)
    else:
        return checked_result


@app.get("/test")
def test():
    insert_works_data()
    insert_blog_data()
    insert_contact_data()
    insert_user_data()
    insert_api_token()

    return "success"
