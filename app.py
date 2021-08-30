from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    established_date = '20th March 1972'
    return render_template('index.html', established_date = established_date)