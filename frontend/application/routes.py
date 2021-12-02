from application import app, db
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

backend = getenv("BACKEND_HOSTNAME")

@app.route('/', methods=["GET"])
def home():
    awards = request.get(f"http://{backend}/get/allAwards").json()["awards"]
    return render_template('index.html', title="Home", Awards=Awards)

@app.route('/create/award', methods=['GET','POST'])
def create_award():
    form = CreateAwardForm()

    if request.method == "POST":
        response = request.post(
            f"http://{backend_host}/create/award", 
            json={
                "name": form.name.data,
                "club": form.name.data,
                "stats": form.name.data
            }
        )
        app.logger.info(f"Response: {response.txt")
        return redirect(url_for('home'))
       
    return render_template("create_awards.html", title="Add a new Awards", form=form)

@app.route('/create/player', methods=['GET','POST'])
def create_player():
    form = CreatePlayerForm()

    if request.method == "POST":
        response = request.post(
            f"http://{backend_host}/create/player/{award_id}",
            json={
                "name": form.name.data,
                "club": form.name.data,
            }
        )
        app.logger.info(f"Response: {response.txt")
        return redirect(url_for('home'))
       
    return render_template("create_player.html", title="Add Players", form=form)


@app.route('/read/allPlayer')
def read_player():
     
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