from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user
from app import db
from app.models import Pitch
from app.main.forms import Pitches

main = Blueprint('main', __name__)


@main.route('/', methods=['GET','POST'])
@main.route('/home', methods=['GET','POST'])
def home():
    form = Pitches()
    pitches = Pitch.query.all()
    if form.validate_on_submit():
        poster = current_user.id
        pitch_created = Pitch(title=form.title.data,description=form.description.data,user_id=poster)
        db.session.add(pitch_created)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('index.html', form=form, pitches=pitches)