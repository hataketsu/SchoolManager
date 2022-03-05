
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
