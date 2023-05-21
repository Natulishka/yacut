from datetime import datetime

from settings import LEN_SHORT_ID

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(LEN_SHORT_ID), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def to_dict(self, host):
        return dict(
            url=self.original,
            short_link=host + self.short,
        )

    def to_dict_short(self):
        return dict(
            url=self.original
        )

    def from_dict(self, data):
        mapping = {'original': 'url',
                   'short': 'custom_id'}
        for field in mapping.keys():
            if mapping[field] in data:
                setattr(self, field, data[mapping[field]])
