from flask import Flask, render_template

from markupsafe import escape

prendas = [
    {"id": 1, "tipo": "pantalon", "talle": 42},
    {"id": 2, "tipo": "pantalon", "talle": 56},
]

app = Flask(__name__)

@app.get("/")                      #este es el "decorador" que indica a qué pedidos responderá nuestra función. Decoradores comienzan con el @ y determinan la ruta y el método.
def home():                                          #el home se escribe como /
    return render_template("home.html")              #es una etiqueta de párrafo de HTML


@app.get("/prendas") 
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>" 



@app.get("/prendas/<int:id>")
def get_prenda(id):
    if id in prendas:
        pren = prendas[id]
        return render_template("prenda.html", id=id, prenda=pren)
    else:
        return("no hay prenda",404)

