from flask import Flask, jsonify
import requests

app = Flask(__name__)


def get_api_data(port, endpoint, code):
    api_url = f"http://127.0.0.1:{port}/api/v1/{endpoint.lower()}/{code}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        api_data = response.json()
        return api_data
    except requests.exceptions.RequestException as e:
        return f"Error fetching data from the API: {e}", 500


@app.route("/api/v1/rappi/<code>")
def get_html(code):
    if code.startswith("AL"):
        api_data = get_api_data("81", "aliados", code)
        html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>HTML Page for AL Type</title>
              </head>
              <body>
                <h1>Data de Aliados</h1>
                <table border="1">
                  <thead>
                    <tr>
                      <th>Categoria</th>
                      <th>Codigo</th>
                      <th>Descripcion</th>
                      <th>PrecioSol</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{api_data[0]['Negocio']}</td>
                      <td>{api_data[0]['Codigo']}</td>
                      <td>{api_data[0]['Apertura']}</td>
                      <td>{api_data[0]['Categoria']}</td>
                    </tr>
                  </tbody>
                </table>
              </body>
            </html>
        """
    elif code.startswith("PRD"):
        api_data = get_api_data("82", "productos", code)
        html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>HTML Page for AL Type</title>
              </head>
              <body>
                <h1>Data de Productos</h1>
                <table border="1">
                  <thead>
                    <tr>
                      <th>Categoria</th>
                      <th>Codigo</th>
                      <th>Descripcion</th>
                      <th>PrecioSol</th>
                      <th>Presentacion</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{api_data[0]['Categoria']}</td>
                      <td>{api_data[0]['Codigo']}</td>
                      <td>{api_data[0]['Descripcion']}</td>
                      <td>{api_data[0]['PrecioSol']}</td>
                      <td>{api_data[0]['Presentacion']}</td>
                    </tr>
                  </tbody>
                </table>
              </body>
            </html>
        """
    else:
        return "Invalid code", 400

    return html_content


if __name__ == "__main__":
    app.run(debug=True)
