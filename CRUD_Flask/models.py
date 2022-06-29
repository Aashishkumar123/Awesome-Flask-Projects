from CRUD_Flask.__init__ import db


class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    course = db.Column(db.String(100),nullable=False)

    def __repr__(self) -> str:
        return f'Student {self.name}'
