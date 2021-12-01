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