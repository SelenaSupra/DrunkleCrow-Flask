from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page='Home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='Info')

@app.route('/seasons')
def seasons():

    now = datetime.now()
    current_year = now.year
    current_month = now.strftime("%B")
    
    return render_template('seasons.html', year = current_year, month=current_month, active_page='Seasons')


@app.route('/corvidcopia')
def corvidcopia():
    return render_template('corvidcopia.html', active_page='CAAAWW!')

@app.route('/ravens')
def ravens():
    return render_template('ravens.html', active_page='Not Her!!')

