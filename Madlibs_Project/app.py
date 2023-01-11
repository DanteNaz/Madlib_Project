
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from flask import Flask, request, render_template





app = Flask(__name__) 

app.config["SECRET_KEY"] = "naz7"
debug = DebugToolbarExtension(app) 






@app.route("/madlibs")
def show_form():                      
    return render_template("words.html")





@app.route("/game")
def get_greeting():                     
 
    noun        = request.args["noun"]            
    place       = request.args["place"]      
    adjective   = request.args["adjective"]      
    verb        = request.args["verb"]      
    term        = request.args["term"]  

    return render_template("game.html", noun=noun, term=term, place=place, adjective=adjective, verb=verb) 




@app.route('/')
def home_page():
    return render_template('home.html')

