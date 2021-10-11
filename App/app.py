"""A simple flask web app"""
from flask import Flask
from flask import render_template

from calc_mod.calculator import Simple
app = Flask(__name__)

@app.route("/")
def index():
    """inded  Route Response"""
    return render_template('index.html')

@app.route("/bad/<value1>/<value2>")
def bad_calc(value1,value2):
    """bad calc Route Response"""
    result = value1 + value2
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response

@app.route("/good/<float:value1>/<float:value2>")
def good_calc(value1,value2):
    """good calc Route Response"""
    calculator = Simple()
    calculator.add(value1,value2)
    response = "The result of the calculation is: " + str(calculator.result) + '<a href="/"> back</a>'
    return response
