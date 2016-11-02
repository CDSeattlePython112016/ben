from flask import Flask, render_template, request, flash, redirect, session
app = Flask(__name__)

app.secret_key = 'andyface4life'


@app.route('/')
def survey():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash('Please enter your name.')
    elif len(request.form['comment']) > 120:
        flash('Your comment cannot be longer than 120 characters.')
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/result')
    return redirect('/')


@app.route('/result')
def result():
    return render_template('result.html')


app.run(debug=True)
