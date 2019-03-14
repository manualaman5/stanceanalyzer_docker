from app import app
from flask import render_template, flash, redirect, url_for
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
        #flash('The requested user is {}'.format(form.twitter_user.data))
        if form.newissue.data != '':
            return redirect(url_for('addissue'))
        elif form.guncontrol.data == False and form.environment.data == False:
            flash('Please, select at least one issue or add one')
            #return redirect(url_for('setup'))
        else:
            return redirect(url_for('results'))
    return render_template('takedata.html', title='Issue set up', form=form)

@app.route('/addissue')
def addissue():
    #newissue = form.newissue.data
    #Here we get the list of examplar accounts for the issue (LIST)
    #accounts = getexamples(newissue)
    return render_template('addissue.html', title='Select example accounts', newissue='newissue')

#@app.route('/addissue2')
#def addissue2():


@app.route('/results')
def results():
    return render_template('results.html', title='Results')