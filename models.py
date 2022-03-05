from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ClassRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class", backref="classroom")

    @property
    def uid(self):
        return f"LH{self.id}"


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class", backref="subject")

    @property
    def uid(self):
        return f"MH{self.id}"

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    subject_taught = db.Column(db.String(100), nullable=False)
    classes = db.relationship("Class", backref="teacher")

    @property
    def uid(self):
        return f"GV{self.id}"

    def __init__(self, first_name, last_name, subject_taught):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_taught = subject_taught


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    classlists = db.relationship("ClassList", backref="student")

    @property
    def uid(self):
        return f"HS{self.id}"

    def __init__(self, first_name, last_name, date_of_birth="0000-00-00 00.00.00"):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


class ClassList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    classes = db.relationship("Class", backref="class_list")


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_room_id = db.Column(db.Integer, db.ForeignKey("class_room.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    class_list_id = db.Column(db.Integer, db.ForeignKey("class_list.id"))

    @property
    def uid(self):
        return f"LH{self.id}"
