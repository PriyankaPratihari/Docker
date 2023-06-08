from fastapi import FastAPI

from core.handler.st_handler import create_book, get_all_data, get_book_id, update_book, delete_book, \
    pipeline_aggregation
from schema.models import Book, Book_up
from core.handler.mail_handler import send_email, Email

app = FastAPI()


@app.post("/books/")
def generate_book(book: Book):
    return create_book(book)


@app.get("/")
def fetch_data():
    return get_all_data()


@app.get("/book_based_on_id/{id}")
def fetch_book_id(_id: int):
    return get_book_id(_id)


@app.put("/books/{book_id}")
def change_book(book_id: int, book: Book_up):
    return update_book(book_id, book)


@app.delete("/books/{book_id}")
def remove_book(book_id: int):
    return delete_book(book_id)


@app.post("/send_email")
def send_item(email: Email):
    return send_email(email)
    # return {"message": "email sent"}


@app.get("/total_book_borrowed")
def get_booked_borrowed():
    """

    :return:
    """
    return pipeline_aggregation()
