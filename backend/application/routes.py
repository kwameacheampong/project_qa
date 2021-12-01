from application import app, db
from application.models import Awards
from application.forms import AwardsForm
from flask import render_template, request, redirect, url_for, jsonify
from os import getenv

@app.route('/')
@app.route('/home')
def home():
    Awards = award.query.all()
    return render_template('index.html', title="Home", Awards=Awards)

@app.route('/create/award', methods=['GET','POST'])
def create_awards():
    form = AwardForm()
    all_Awards = request.get(f"http://{backend_host}/read/allAwards").json()
    for award in all_Awards["awards"]:
      form.award.choices.append((award[id], award["name"]))

    if request.method == "POST":
        response = request.post(f"http://{backend_host}/create/award", json={"name": form.name.data})
        new_awards = Awards(description=form.description.data)
        app.logger.info(f"Response: {response.txt")
        return redirect(url_for('home'))

    return render_template("create_awards.html", title="Add a new awards", form=form)

@app.route('/read/allAwards')
def read_awards():
     
    Awards = award.query.all()
    awards_dict = {"awards": []}
    for awards in Awards:
        awards_dict["awards"].append(   
                      {
                "description": awards.description,
                "completed": awards.completed
            }
        )
    return jsonify(awards_dict)

@app.route('/update/awards/<int:id>', methods=['GET','POST'])
def update_Awards(id):
    form = AwardsForm()
    awards = Awards.query.get(id)

    if request.method == "POST":
        awards.description = form.description.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_awards.html', awards=awards, form=form)

@app.route('/delete/awards/<int:id>')
def delete_Awards(id):
    awards = Awards.query.get(id)
    db.session.delete(awards)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/complete/awards/<int:id>')
def complete_Awards(id):
    awards = Awards.query.get(id)
    awards.completed = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/incomplete/awards/<int:id>')
def incomplete_Awards(id):
    awards = Awards.query.get(id)
    awards.completed = False
    db.session.commit()
    return redirect(url_for('home'))