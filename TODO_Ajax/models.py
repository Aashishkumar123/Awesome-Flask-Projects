from TODO_Ajax.__init__ import db


class List(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)

    def __repr__(self) -> str:
        return f'<List {self.title}>'
