from datetime import datetime

from settings import LENGTH_MAX
from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(255), nullable=False)
    short = db.Column(db.String(LENGTH_MAX), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def to_dict(self):
        return dict(url=self.original,
                    short_link=self.short)
