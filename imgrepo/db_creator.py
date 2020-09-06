from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///nutrition.db', echo=True)
Base = declarative_base()


class ImageName(Base):
    __tablename__ = "imagenames"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<ImageName: {}>".format(self.name)


class Album(Base):
    """"""
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)
    publisher = Column(String)
    media_type = Column(String)

    imagename_id = Column(Integer, ForeignKey("imagenames.id"))
    imagename = relationship("ImageName", backref=backref(
        "albums", order_by=id))


# create tables
Base.metadata.create_all(engine)