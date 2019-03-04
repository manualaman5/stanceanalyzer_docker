from app import app
from flask import render_template, flash, redirect
from app.takedata import TakeData

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'Manuel'}
    posts = [
    {'author': {'username': 'John'},'body': 'Beautiful day in Portland!'},
    {'author': {'username': 'Susan'},'body': 'The Avengers movie was so cool!'}
    ]
    return render_template('home.html', title='Home', user=user, posts=posts)
@app.route('/setup', methods=['GET', 'POST'])
def setup():
    form = TakeData()
    if form.validate_on_submit():
        flash('The requested user is {}'.format(
            form.twitter_user.data))
        return redirect('/index')
    return render_template('takedata.html', title='Issue set up', form=form)

@app.route('/addissue')
def addissue():
    return render_template('addissue.html', title='Add issue')

@app.route('/results')
def results():
    return render_template('results.html', title='Results')