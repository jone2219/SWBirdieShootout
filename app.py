from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    # dev database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ketter1ng@localhost/SWBirdieShootout'
else:
    app.debug = False
    # prod database
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300


db = SQLAlchemy(app)


class ScoreEntry(db.Model):
    __tablename__ = 'Players'
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(200), unique=True)

    # finish scores table
    __tablename__ = 'Scores'
    player = db.Column(db.String(200))

    def __init__(self, player, date, hole1-18):
        self.player = player
        # etc


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        player = request.form['PlayerName']
        date = request.form['date_played']
        h1 = request.form['Hole1']
        h2 = request.form['Hole2']
        h3 = request.form['Hole3']
        h4 = request.form['Hole4']
        h5 = request.form['Hole5']
        h6 = request.form['Hole6']
        h7 = request.form['Hole7']
        h8 = request.form['Hole8']
        h9 = request.form['Hole9']
        h10 = request.form['Hole10']
        h11 = request.form['Hole11']
        h12 = request.form['Hole12']
        h13 = request.form['Hole13']
        h14 = request.form['Hole14']
        h15 = request.form['Hole15']
        h16 = request.form['Hole16']
        h17 = request.form['Hole17']
        h18 = request.form['Hole18']

        #holes_print = ", ".join([f"h{i}" for i in range(1, 19)])
        if player == '' or player == 'Select your name':
            return render_template('index.html', message='Please select your name from the dropdown')
        if date == '':
            return render_template('index.html', message='Please select a date')

        print(player, date, h1, h2, h3, h4, h5, h6, h7, h8,
              h9, h10, h11, h12, h13, h14, h15, h16, h17, h18)
        # this is temporary and for example only - change this to some other Success page later
        return render_template('users.html')


if __name__ == '__main__':
    app.run()
