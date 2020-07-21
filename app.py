from flask import Flask, render_template, flash, redirect, url_for
import os
import random
from takedata import TakeData
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
@app.route('/index')
def index():
    return render_template('home.html', title='Home')

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    form = TakeData()
    if form.validate_on_submit():
        flash('The requested user is {}'.format(form.twitter_user.data))
        if form.newissue.data != '':
            return redirect(url_for('addissue'))
        elif form.guncontrol.data == False and form.environment.data == False:
            flash('Please, select at least one issue or add one')
            return redirect(url_for('setup'))
        else:
            return redirect(url_for('results'))
    return render_template('takedata.html', title='Issue set up', form=form)
@app.route('/addissue')
def addissue():
    return render_template('addissue.html', title='Select example accounts', newissue='newissue')

@app.route('/results')
def results():
    return render_template('results.html', title='Results')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
