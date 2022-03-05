from flask import Blueprint
from flask import render_template, request, url_for, redirect, flash

from models import ClassRoom
from models import db

class_room_bp = Blueprint("class_room", __name__)


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
