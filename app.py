from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pet
from form import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():
    """Show home page"""
    return render_template("home_page.html")

@app.rotue("/add")
def show_pet():
    pet = Pet.query.all()

    return render_template("home_page.html", pet = pet)

@app.rotue("/add", methods = ["GET","POST"])
def handle_pet():
    """Renders pet form (GET) or handles pet form submission (POST)"""
    form = AddPetForm
    if form.validate_on_submit():
        name = form.name.data
        speices = form.speices.data
        photo = form.photo.data
        age = form.age.data
        note = form.note.data
        available = form.available.data
        flash(f"You adopted {name}. This dog is {speices}. Here is a {photo}. The dog age is {age}. Here are some {note} about him/her. If the dog is {available}")
    else:
        return render_template("add_pet_form.html")


@app.rotue("/add", methods = ["GET","POST"])
def add_pet():
    form = AddPetForm
    pet = db.session.query(Pet.name, Pet.speices, Pet.photo, Pet.age, Pet.notes)
    form.name.choices = pet

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        speices = form.speices.data
        photo = form.photo.data
        age = form.age.data
        note = form.note.data

        new_pet = Pet(id,name=name, speices=speices, photo=photo, age=age, note=note)
        db.session.add(new_pet)
        db.session.commit()
        
        return redirect("/")
    else:
        return render_template("add_pet_form.html")

@app.route("/<int:pet.id", methods=["GET", "POST"])
def edit_pet():
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj = pet)
    adoption_agency = db.session.query(Pet.photo, Pet.notes)
    form.photo.choices = adoption_agency
    if form.validate_on_submit():
        pet.photo = form.photo.data
        pet.note = form.note.data
        pet.available = form.available.data

        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet.html", form = form)
    
@app.route("/<int:pet.id>", ["GET","POST"])    
def hand_edit_pet():
    """Renders pet form (GET) or handles pet form submission (POST)"""
    form = AddPetForm
    if form.validate_on_submit():
        photo = form.photo.data
        note = form.note.data
        available = form.available.data
        flash(f"The things that you can edit are {photo}, {note}, and {available}")
    else:
        return render_template("edit_pet.html")