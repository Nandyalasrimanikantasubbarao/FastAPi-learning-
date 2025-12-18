from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)


Books = []


@app.get("/")
def helloWorld():
    return Books


# @app.get("/{name}")
# def readName(name):
#     return {"hello": name}


@app.post("/")
def createBook(book: Book):
    Books.append(book)
    return book


@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    counter = 0
    for x in Books:
        counter += 1
        if x.id == book_id:
            Books[counter - 1] = book
            return Books[counter - 1]
    return HTTPException(status_code=404, detail=f"ID {book_id}: Does not exist")


@app.delete("/{Book_id}")
def delete_book(book_id: UUID):
    counter = 0
    for x in Books:
        counter += 1
        if x.id == book_id:
            del Books[counter - 1]
            return f"ID: {book_id} deleted"
    return HTTPException(status_code=404, detail=f"ID {book_id} :Does not exist")
