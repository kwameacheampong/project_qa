from application import app
from flask import render_template, request, redirect, url_for, jsonify
from application.forms import FlaskForm
import requests
from os import getenv

backend = "award-project_backend:5000"

@app.route('/', methods=["GET"])
def home():
    award = requests.get (f"http://{backend}/get Allaward").json()["awards"]
    return render_template('index.html', title="Home", awards=awards)

@app.route('/create/awards', methods=['GET','POST'])
def create_awards():
    form = CreateAwardsForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend}/create/awards", 
            json={
                "name": form.name.data,
                "club": form.name.data,
                "stats": form.name.data
            }
        )
        app.logger.info(f"Response: {response.txt}")
        return redirect(url_for('home'))
       
    return render_template("create_awards.html", title="Add a new awards", form=form)

@app.route('/create/players', methods=['GET','POST'])
def create_players():
    form = CreatePlayersForm()

    if request.method == "POST":
        response = requests.post(
            f"http://{backend}/create/players/{award_id}",
            json={
                "name": form.name.data,
                "club": form.name.data,
            }
        )
        app.logger.info(f"Response: {response.txt}")
        return redirect(url_for('home'))
       
    return render_template("create_players.html", title="Add alayers", form=form)


@app.route('/read/allPlayers')
def read_players():
     
    Awards = award.query.all()
    awards_dict = {"awards": []}
    for award in Awards:
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

    if requests.method == "POST":
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