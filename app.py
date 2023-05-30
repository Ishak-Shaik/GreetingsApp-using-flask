from flask import Flask, render_template , request, flash

app=Flask(__name__)
app.secret_key='asdfghj'

@app.route('/')

def index():
    flash("What's your name?")
    return render_template('index.html')

@app.route('/greet',methods=['GET','POST'])

def greet():
    flash('Hi '+str(request.form['name'])+', great to see you!')
    return render_template('index.html')