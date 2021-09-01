from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    established_date = '21st March 1970'
    return render_template('index.html', established_date = established_date)