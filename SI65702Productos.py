import flask
from flask import Flask, redirect, url_for, request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Creacion de data
productos = [
    {
        "Codigo": "PRD01",
        "Categoria": "Supermercados",
        "Descripcion": "La Calera Huevos Pardos",
        "Presentacion": "30 unid",
        "PrecioSol": 21.3,
    },
    {
        "Codigo": "PRD02",
        "Categoria": "Supermercados",
        "Descripcion": "Coca Cola Bebida gaseosa",
        "Presentacion": "500 ml",
        "PrecioSol": 2.9,
    },
    {
        "Codigo": "PRD03",
        "Categoria": "Supermercados",
        "Descripcion": "Coca Cola Gaseos sin Azucar",
        "Presentacion": "1.5 l",
        "PrecioSol": 7.9,
    },
    {
        "Codigo": "PRD04",
        "Categoria": "Supermercados",
        "Descripcion": "Donofrio Bombones de Helado",
        "Presentacion": "216 ml",
        "PrecioSol": 19.47,
    },
    {
        "Codigo": "PRD05",
        "Categoria": "Supermercados",
        "Descripcion": "San mateo Agua Mineral",
        "Presentacion": "2500 ml",
        "PrecioSol": 2.68,
    },
    {
        "Codigo": "PRD06",
        "Categoria": "Supermercados",
        "Descripcion": "Inka Chips papa Frita sabor Jalape o",
        "Presentacion": "135 gr",
        "PrecioSol": 10.82,
    },
    {
        "Codigo": "PRD07",
        "Categoria": "Supermercados",
        "Descripcion": "Fanta sabor Naranja",
        "Presentacion": "500 ml",
        "PrecioSol": 2.5,
    },
    {
        "Codigo": "PRD08",
        "Categoria": "Supermercados",
        "Descripcion": "Pilsen Callao Cerveza en lata 6",
        "Presentacion": "355 ml",
        "PrecioSol": 25.9,
    },
    {
        "Codigo": "PRD09",
        "Categoria": "Supermercados",
        "Descripcion": "Don Mamino Pan Cachito",
        "Presentacion": "6 und",
        "PrecioSol": 9.7,
    },
    {
        "Codigo": "PRD10",
        "Categoria": "Supermercados",
        "Descripcion": "Florida Filete de Atun en aceite",
        "Presentacion": "170 gr",
        "PrecioSol": 6.4,
    },
    {
        "Codigo": "PRD11",
        "Categoria": "Supermercados",
        "Descripcion": "Campomar Trozos e Atun en aceite",
        "Presentacion": "160 gr",
        "PrecioSol": 5.9,
    },
    {
        "Codigo": "PRD12",
        "Categoria": "Supermercados",
        "Descripcion": "Coste o Blanco Extra Grande",
        "Presentacion": "750 gr",
        "PrecioSol": 4.5,
    },
    {
        "Codigo": "PRD13",
        "Categoria": "Supermercados",
        "Descripcion": "Paisana Arroz Blanco Superior ",
        "Presentacion": "5 Kg",
        "PrecioSol": 23.1,
    },
]


@app.route("/api/v1/productos", methods=["GET"])
def api_all():
    return jsonify(productos)


@app.route("/api/v1/productos/<string:url>", methods=["GET"])
def products(url):
    print(url)
    results = []
    for producto in productos:
        print(producto)
        if producto["Codigo"] == url:
            results.append(producto)
    return jsonify(results)


@app.route("/api/v1/catproducto/<string:categoria>", methods=["GET"])
def categorias(categoria):
    print(categoria)
    results = []
    for producto in productos:
        print(producto)
        if producto["Categoria"] == categoria:
            results.append(producto)
    return jsonify(results)


app.run(host="0.0.0.0", port=82)
