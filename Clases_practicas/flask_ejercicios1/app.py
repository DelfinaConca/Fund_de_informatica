from flask import Flask, render_template

from markupsafe import escape

app = Flask(__name__)

@app.get("/")                                         
def home():                                            
    return render_template("home.html")              

