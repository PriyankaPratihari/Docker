from core.db.mongo_db import lib
from schema.models import Book, Book_up


# Create a new book


def create_book(book: Book):
    try:
        existing_book = lib.find_one({"id": book.id})

        if existing_book:
            raise Exception("Book ID already exists")

        lib.insert_one(book.dict())
        return {"message": "Book created successfully"}

    except Exception as e:
        return {"message": str(e)}


def get_all_data():
    return {
        "details": [{'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
                    for book in lib.find({})]}


def get_book_id(_id: int):
    books = lib.find({})
    details = []
    for book in books:
        if book['id'] == id:
            detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
            details.append(detail)
    return {"details": details}


def update_book(book_id: int, book: Book_up):
    result = lib.update_one({"id": book_id}, {"$set": book.dict()})

    if result.modified_count > 0:
        return {"message": "Book updated successfully"}
    else:
        return {"error": "Book not found"}


# Delete a book
def delete_book(book_id: int):
    result = lib.delete_one({"id": book_id})

    if result.deleted_count > 0:
        return {"message": "Book deleted successfully"}
    else:
        return {"error": "Book not found"}


def pipeline_aggregation():
    pipeline = [
        {
            '$project': {
                '_id': 0
            }
        },
        {
            '$match': {
                'borrowed': False
            }
        },
        {
            '$group': {
                '_id': None,
                'total': {
                    '$sum': 1
                }
            }
        },
        {
            '$project': {
                '_id': 0
            }
        }
    ]
    data = lib.aggregate(pipeline)
    data = list(data)
    return {"total book in lib": data[0]['total']}
