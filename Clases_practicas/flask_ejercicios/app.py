from flask import Flask, render_template

from markupsafe import escape

app = Flask(__name__)

@app.get("/")                                         
def home():                                            
    return render_template("home.html")              

@app.get("/resultados/") 
def get_all_resultados():
    return render_template("rtados.html") 


@app.get("/plan_2023/") 
def get_all_plan():
    return render_template("plan.html") 