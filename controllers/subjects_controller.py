


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

