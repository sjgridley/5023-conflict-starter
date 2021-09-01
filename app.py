from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def history():
    established_date = '22nd March 1971'
    return render_template('index.html', established_date = established_date)