from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

productos = {
1: {"name": "Shampoo sólido", "Stock": 5, "Precio_unitario": 300},
2: {"name": "Crema de manos", "Stock": 6, "Precio_unitario": 600},
3: {"name":"jabon liquido" ,"Stcok":9, "Precio_unitario":500}}



@app.get("/")
def home():
    return render_template("home.html")

@app.get("/productos/")
def get_all_products():
    return render_template("productos.html", productos=productos.items())

@app.get("/productos/<int:id>")
def get_producto(id):
    if id in productos:
        producto = productos[id]
        return render_template('producto.html', id=id, prod=producto)
    else:
        return ("no hay producto", 404)
    
