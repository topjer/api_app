import datetime
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from .crud import (
    create_entry,
    delete_entry,
    get_all_entries,
    get_entry,
    get_long_url,
)
from .database import base, engine, my_sessionmaker
from .schemas import Input, MetaData
from .url_tools import shorten_string

STRING_LENGTH = 8

base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    """Provide database session

    Not entirely sure what this does tbh

    :yield:
        database sessions
    """
    db = my_sessionmaker
    try:
        yield db()
    finally:
        db.close_all()


@app.get("/")
async def root():
    """Display message at root"""
    return {"message": "Hello World!"}


@app.post("/add_url/")
async def add_url(entry: Input, db: Session = Depends(get_db)):
    """Add a given URL

    Short URL is being created. MetaData object is being created and
    added to database.

    :param entry:
        contains the necessary input data
    :param db:
        database session
    """
    short_url = shorten_string(entry.url, string_length=STRING_LENGTH)

    if get_entry(db, short_url):
        raise HTTPException(status_code=400, detail="Short-url is already in database.")
    meta_data = dict()
    meta_data["long_url"] = entry.url
    meta_data["description"] = entry.description
    meta_data["short_url"] = short_url
    meta_data["created"] = str(datetime.now())
    md_object = MetaData(**meta_data)
    create_entry(db, md_object)
    return {"message": f"{entry.url} was added.", "short_url": short_url}


@app.get("/list_urls/")
async def list_urls(db: Session = Depends(get_db)):
    """List all registered urls

    :param db:
        database session
    """
    output = get_all_entries(db)
    return output


@app.get("/redirect/{short_url}")
async def return_redirect(short_url: str, db: Session = Depends(get_db)):
    """Return the redirect for a given short url

    :param short_url:
        short url in question
    :param db:
        database session
    :return:
    """
    long_url = get_long_url(db, short_url)
    if not long_url:
        raise HTTPException(
            status_code=400, detail="Nothing was found for the specified short_url"
        )

    return RedirectResponse(long_url)


@app.delete("/delete_entry/{short_url}")
async def delete(short_url: str, db: Session = Depends(get_db)):
    return delete_entry(db, short_url)
