from app import db


class ImageName(db.Model):
    __tablename__ = "imagenames"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)


class Album(db.Model):
    """"""
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String)
    publisher = db.Column(db.String)
    media_type = db.Column(db.String)

    imagename_id = db.Column(db.Integer, db.ForeignKey("imagenames.id"))
    imagename = db.relationship("ImageName", backref=db.backref(
        "albums", order_by=id), lazy=True)
