from application import app, db
from application.models import Awards
from application.forms import AwardsForm
from flask import render_template, request, redirect, url_for, jsonify
from os import getenv

@app.route('/')
@app.route('/home')
def home():
    all_awards = awards.query.all()
    return render_template('index.html', title="Home", all_awards=all_awards)

@app.route('/create/player/<int:award_id>', methods=['GET','POST'])
def create_player(award_id):
    json = request.json
    new_player = Player(
        name = json["name"],
        award_id = award_id,
        stats = json["stats"]
    )
        db.session.add(new_award)
        db.session.commit()
    return render_template("create_award.html", title="Add a new Award", form=form)

@app.route('/get/allawards', method=["GET"])
def get_all_awards():
    all_awards = Awards.query.all()
    json = {"awards": []}
    for award in all_awards:
        player =[]
        for player in award.players:
            award.append(        
            {
                "id": award.id,
                "name": player.
            }
        )
    return jsonify(awards_dict)

@app.route('/update/award/<int:id>', methods=['GET','POST'])
def update_award(id):
    form = AwardForm()
    award = Awards.query.get(id)

    if request.method == "POST":
        award.description = form.description.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_award.html', award=award, form=form)

@app.route('/delete/award/<int:id>')
def delete_Award(id):
    award = Awards.query.get(id)
    db.session.delete(award)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/complete/award/<int:id>')
def complete_Award(id):
    award = awards.query.get(id)
    award.completed = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/incomplete/award/<int:id>')
def incomplete_awards(id):
    awards = Awards.query.get(id)
    awards.completed = False
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/create/award', methods=['GET','POST'])
def create_awards():
    form = AwardsForm()

    if request.method == "POST":
        new_awards = Awardss(description=form.description.data)
        db.session.add(new_awards)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_award.html", title="Add a new Award", form=form)

 @app.route('/create/award', methods=['GET','POST'])
def create_award():
    form = awardsForm()

    if request.method == "POST":
        new_awards = awardss(description=form.description.data)
        db.session.add(new_award)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_award.html", title="Add a new Award", form=form)

@app.route('/create/award', methods=['GET','POST'])
def create_award():
    form = awardsForm()

    if request.method == "POST":
        new_award = Award(description=form.description.data)
        db.session.add(new_award)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_award.html", title="Add a new Award", form=form)           