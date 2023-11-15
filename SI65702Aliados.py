import flask
from flask import Flask, redirect, url_for, request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Creacion de data
aliados = [
    {
        "Codigo": "AL001",
        "Negocio": "SPID",
        "Apertura": "08:00 a. m.",
        "Categoria": "Express",
    },
    {
        "Codigo": "AL002",
        "Negocio": "OXXO",
        "Apertura": "08:00 a. m.",
        "Categoria": "Express",
    },
    {
        "Codigo": "AL003",
        "Negocio": "Listo",
        "Apertura": "08:00 a. m.",
        "Categoria": "Express",
    },
    {
        "Codigo": "AL004",
        "Negocio": "Metro",
        "Apertura": "08:00 a. m.",
        "Categoria": "Express",
    },
    {
        "Codigo": "AL005",
        "Negocio": "CoolBox",
        "Apertura": "09:00 a. m.",
        "Categoria": "Tiendas",
    },
    {
        "Codigo": "AL006",
        "Negocio": "Xiaomi",
        "Apertura": "09:00 a. m.",
        "Categoria": "Tiendas",
    },
    {
        "Codigo": "AL007",
        "Negocio": "Phantom",
        "Apertura": "09:00 a. m.",
        "Categoria": "Tiendas",
    },
    {
        "Codigo": "AL008",
        "Negocio": "Sony",
        "Apertura": "09:00 a. m.",
        "Categoria": "Tiendas",
    },
    {
        "Codigo": "AL009",
        "Negocio": "Wong",
        "Apertura": "09:00 a. m.",
        "Categoria": "Supermercados",
    },
    {
        "Codigo": "AL010",
        "Negocio": "Spid",
        "Apertura": "09:00 a. m.",
        "Categoria": "Supermercados",
    },
    {
        "Codigo": "AL011",
        "Negocio": "La Cesta",
        "Apertura": "09:00 a. m.",
        "Categoria": "Supermercados",
    },
    {
        "Codigo": "AL012",
        "Negocio": "Flora & Fauna",
        "Apertura": "09:00 a. m.",
        "Categoria": "Supermercados",
    },
    {
        "Codigo": "AL013",
        "Negocio": "Freshmart",
        "Apertura": "09:00 a. m.",
        "Categoria": "Supermercados",
    },
    {
        "Codigo": "AL014",
        "Negocio": "Bembos",
        "Apertura": "09:00 a. m.",
        "Categoria": "Restaurantes",
    },
    {
        "Codigo": "AL015",
        "Negocio": "La Panka",
        "Apertura": "09:00 a. m.",
        "Categoria": "Restaurantes",
    },
    {
        "Codigo": "AL016",
        "Negocio": "Rockys",
        "Apertura": "09:00 a. m.",
        "Categoria": "Restaurantes",
    },
]


@app.route("/api/v1/aliados", methods=["GET"])
def api_all():
    return jsonify(aliados)


@app.route("/api/v1/aliados/<string:url>", methods=["GET"])
def products(url):
    print(url)
    results = []
    for aliado in aliados:
        print(aliado)
        if aliado["Codigo"] == url:
            results.append(aliado)
    return jsonify(results)


@app.route("/api/v1/categoria/<string:categoria>", methods=["GET"])
def categorias(categoria):
    print(categoria)
    results = []
    for aliado in aliados:
        print(aliado)
        if aliado["Categoria"] == categoria:
            results.append(aliado)
    return jsonify(results)


app.run(host="0.0.0.0", port=81)
