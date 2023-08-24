import requests
import configparser
from flask import Flask, render_template, request
from utils import get_sweeping_time

app = Flask(__name__)


@app.route('/')
def parheeze_jarimeh():
    return render_template('home.html')


@app.route('/results', methods=['POST', "POST"])
def render_results():
    street_name = request.form['sname']
    street_num = request.form['streetnum']
    return get_sweeping_time(street_num, street_name)


if __name__ == "__main__":
    app.run()