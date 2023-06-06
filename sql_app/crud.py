from sqlalchemy.orm import Session

from . import models, schemas


def empty_table(db: Session):
    """Delete everything from url_data table

    For testing purposes

    :param db:
        database session
    """
    db.execute("delete from url_data")
    db.commit()


def create_entry(db: Session, metadata: schemas.MetaData):
    """add entry to url_data table

    :param db:
        database sessions
    :param metadata:
        contains all metadata defining an entry
    :return:
        create urlData object
    """
    db_url_data = models.UrlData(**metadata.__dict__)
    db.add(db_url_data)
    db.commit()
    db.refresh(db_url_data)
    return db_url_data


def get_entry(db: Session, short_url: str):
    """Queries database for short_url

    :param db:
        database session
    :param short_url:
        short_url in question
    :return:
    """
    return (
        db.query(models.UrlData).filter(models.UrlData.short_url == short_url).first()
    )


def get_all_entries(db: Session):
    """queries all entries from url_data table

    :param db:
        database session
    :return:
    """
    return db.query(models.UrlData).all()


def get_long_url(db: Session, short_url: str):
    """Query long url for a specific short url

    Number of klicks is being increased in the process.

    :param db:
        database session
    :param short_url:
        short url in question
    :return:
        long url belonging to the corresponding short url
    """
    result = (
        db.query(models.UrlData).filter(models.UrlData.short_url == short_url).first()
    )
    if hasattr(result, "klicks"):
        # not the best way to do this, better would be to log all access in database and then
        # determine number of those as number of clicks
        result.klicks = result.klicks + 1
        db.commit()
    return result.long_url if hasattr(result, "long_url") else None


def delete_entry(db: Session, short_url: str):
    result = (
        db.query(models.UrlData).filter(models.UrlData.short_url == short_url).delete()
    )
    db.commit()
    if result:
        return_string = f"{short_url} has been removed."
    else:
        return_string = (
            f"{short_url} was not found in database. Nothing has been removed."
        )

    return {"message": return_string}
