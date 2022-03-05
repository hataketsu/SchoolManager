from flask import Blueprint
from flask import render_template, url_for, redirect, flash

from forms import EditClassRoomForm
from models import ClassRoom
from models import db

class_room_bp = Blueprint("class_room", __name__)


@class_room_bp.route("/")
def class_rooms_list():
    class_rooms = ClassRoom.query.all()
    return render_template("class_rooms.html", class_rooms=class_rooms, title="Class rooms")


@class_room_bp.route("/create", methods=["GET", "POST"])
def create():
    form = EditClassRoomForm()
    if form.validate_on_submit():
        class_room = ClassRoom()
        class_room.capacity = form.capacity.data
        db.session.add(class_room)
        db.session.commit()
        flash("Successed!")
        return redirect(url_for("class_room.class_rooms_list"))
    return render_template("form.html", form=form, title="Add new class room")


@class_room_bp.route("/edit/<_id>", methods=["post", "get"])
def edit(_id):
    class_room = ClassRoom.query.get_or_404(_id)
    form = EditClassRoomForm()

    if form.validate_on_submit():
        class_room.capacity = form.capacity.data
        db.session.add(class_room)
        db.session.commit()
        flash("Success!")
        return redirect(url_for("class_room.class_rooms_list"))
    else:
        form.capacity.data = class_room.capacity
    return render_template("form.html", form=form, title="Edit class room")


@class_room_bp.route("/delete/<_id>")
def delete(_id):
    del_classroom = ClassRoom.query.get_or_404(_id)
    db.session.delete(del_classroom)
    db.session.commit()

    flash("Deleted!")
    return redirect(url_for("class_room.class_rooms_list"))
