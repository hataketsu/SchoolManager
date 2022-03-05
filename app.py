from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "hello_world"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://minhduc@localhost/minhduc"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db"
db = SQLAlchemy(app)


class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class", backref="classroom")

    @property
    def uid(self):
        return f"LH{self.id}"

    def __init__(self, capacity):
        self.capacity = capacity


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
    class_room_id = db.Column(db.Integer, db.ForeignKey("classroom.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    class_list_id = db.Column(db.Integer, db.ForeignKey("class_list.id"))

    @property
    def uid(self):
        return f"LH{self.id}"


@app.route("/")
@app.route("/home")
def trang_chu():
    return render_template("home.html", title="Home")


@app.route("/class_rooms")
def class_rooms():
    classrooms = Classroom.query.all()
    return render_template("class_rooms.html", classrooms=classrooms, title="Classroom")


@app.route("/class_rooms/insert", methods=["POST"])
def insert_class_rooms():
    if request.method == "POST":
        capacity = request.form["capacity"]

        classroom_insert = Classroom(capacity)
        db.session.add(classroom_insert)
        db.session.commit()

        flash("Successed!")

        return redirect(url_for("class_rooms"))


@app.route("/class_rooms/update", methods=["GET", "POST"])
def update_class_rooms():
    if request.method == "POST":
        edit_classroom = Classroom.query.get(request.form.get("id"))

        edit_classroom.capacity = request.form["capacity"]

        db.session.commit()

        flash("Successed!")

        return redirect(url_for("class_rooms"))


@app.route("/class_rooms/delete/<id>/", methods=["GET", "POST"])
def delete_class_rooms(id):
    del_classroom = Classroom.query.get(id)
    db.session.delete(del_classroom)
    db.session.commit()

    flash("Deleted!")

    return redirect(url_for("class_rooms"))


@app.route("/hoc_sinh")
def hoc_sinh():
    students = Student.query.all()
    return render_template("hoc_sinh.html", students=students, title="Student")


@app.route("/hoc_sinh/insert", methods=["POST"])
def insert_hoc_sinh():
    if request.method == "POST":
        firstname = request.form["first_name"]
        lastname = request.form["last_name"]
        date_of_birth = request.form["date_of_birth"]

        student_insert = Student(firstname, lastname, date_of_birth)
        db.session.add(student_insert)
        db.session.commit()

        flash("Successed!")

        return redirect(url_for("hoc_sinh"))


@app.route("/hoc_sinh/update", methods=["GET", "POST"])
def update_hoc_sinh():
    if request.method == "POST":
        edit_student = Student.query.get(request.form.get("id"))

        edit_student.first_name = request.form["first_name"]
        edit_student.last_name = request.form["last_name"]
        edit_student.date_of_birth = request.form["date_of_birth"]

        db.session.commit()

        flash("Successed!")

        return redirect(url_for("hoc_sinh"))


@app.route("/hoc_sinh/delete/<id>/", methods=["GET", "POST"])
def delete_hoc_sinh(id):
    del_student = Student.query.get(id)
    db.session.delete(del_student)
    db.session.commit()

    flash("Deleted!")

    return redirect(url_for("hoc_sinh"))


@app.route("/mon_hoc")
def mon_hoc():
    subjects = Subject.query.all()
    return render_template("mon_hoc.html", subjects=subjects, title="Subject")


@app.route("/mon_hoc/insert", methods=["POST"])
def insert_mon_hoc():
    if request.method == "POST":
        name = request.form["name"]
        capacity = request.form["capacity"]

        subject_insert = Subject(name, capacity)
        db.session.add(subject_insert)
        db.session.commit()

        flash("Successed!")

        return redirect(url_for("mon_hoc"))


@app.route("/mon_hoc/update", methods=["GET", "POST"])
def update_mon_hoc():
    if request.method == "POST":
        edit_subject = Subject.query.get(request.form.get("id"))

        edit_subject.name = request.form["name"]
        edit_subject.capacity = request.form["capacity"]

        db.session.commit()

        flash("Successed!")

        return redirect(url_for("mon_hoc"))


@app.route("/mon_hoc/delete/<id>/", methods=["GET", "POST"])
def delete_mon_hoc(id):
    del_subject = Subject.query.get(id)
    db.session.delete(del_subject)
    db.session.commit()

    flash("Deleted!")

    return redirect(url_for("mon_hoc"))


@app.route("/giao_vien")
def giao_vien():
    teachers = Teacher.query.all()
    return render_template("giao_vien.html", teachers=teachers, title="Teacher")


@app.route("/giao_vien/insert", methods=["POST"])
def insert_giao_vien():
    if request.method == "POST":
        firstname = request.form["first_name"]
        lastname = request.form["last_name"]
        subject_taught = request.form["subject_taught"]

        teacher_insert = Teacher(firstname, lastname, subject_taught)
        db.session.add(teacher_insert)
        db.session.commit()

        flash("Successed!")

        return redirect(url_for("giao_vien"))


@app.route("/giao_vien/update", methods=["GET", "POST"])
def update_giao_vien():
    if request.method == "POST":
        edit_teacher = Teacher.query.get(request.form.get("id"))

        edit_teacher.first_name = request.form["first_name"]
        edit_teacher.last_name = request.form["last_name"]
        edit_teacher.subject_taught = request.form["subject_taught"]

        db.session.commit()

        flash("Successed!")

        return redirect(url_for("giao_vien"))


@app.route("/giao_vien/delete/<id>/", methods=["GET", "POST"])
def delete_giao_vien(id):
    del_teacher = Teacher.query.get(id)
    db.session.delete(del_teacher)
    db.session.commit()

    flash("Deleted!")

    return redirect(url_for("giao_vien"))


if __name__ == "__main__":
    app.run(debug=True)
