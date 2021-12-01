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

@app.route('/create/award', methods=['POST'])
def create_awards():
    json = request.json
    new_award = Award(
        name = json["name"],
        club = json["club"]
        stats = json["stats"]
    )
    db.session.add(new_award)
    db.session.commit()
    return f"Award '{new_award.name}'' added to database"

@app.route('/create/players/<int:id>', methods=['GET','POST'])
def create_player(award_id):
     json = request.json
    new_award = Award(
        name = json["name"],
        award_id = award_id,
        club = json["club"]
        stats = json["stats"]
    )
    db.session.add(new_award)
    db.session.commit()
    return f"Award '{new_award.name}' added to database"

@app.route('/get/allAwards', methods=["GET"])
def get_all_awards():
    all_awards =Award.query.all()
    json = {"awards": []}
    for award in all_Awards:
        player = []
        for player in award.players:
            player.append(
                {
                    "id": [player.id,
                    "name": player.name,
                    "award": player.award_id,
                    "club": player.club
                }
            )
        json["awards"].append(
            {
                "id":award.id,
                "name": award.name,
                "club": award.club,
                "stats":award.stats,
                "player": players
            }                    
        )
    return jsonify(json)

@app.route('/get/allPlayers/<int:id>', methods=['GET'])
def get_player(id):     
    players =Award.query.get(id).players
    json = {"players": []}
    for player in players:        
            json["players"].append(
                {
                    "id": [player.id,
                    "name": player.name,
                    "award": player.award_id,
                    "club": player.club
                }
            )
        return jsonify(json)

@app.route('/update/awards/<int:id>')
def update_Awards(id):
    data = request.json
    awards = Awards.query.get(id)
    awards.updated = True
    db.session.commit()
    return redirect(url_for('home'))

