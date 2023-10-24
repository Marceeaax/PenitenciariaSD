import json
from flask import Flask, jsonify, request, abort, Response
from flask_cors import CORS
    
app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII'] = False

# Load the data from the JSON file
with open('reclusos_ficticios_1000_completo.json', 'r', encoding='utf-8') as file:
    reclusos_data = json.load(file)


@app.route('/Reclusos', methods=['GET'])
def get_reclusos():
    page = request.args.get('pagina', 1, type=int)
    per_page = request.args.get('cantidad', 10, type=int)
    
    # Pagination logic
    start = (page - 1) * per_page
    end = start + per_page

    # Exclude properties here
    exclude_properties = ["enfermedades", "visitantes", "llamadas", "sentencia", "abogado", "pabellon", "celda_nro"]
    result = []
    for recluso in reclusos_data[start:end]:
        data = {key: value for key, value in recluso.items() if key not in exclude_properties}
        result.append(data)

    return jsonify(result)


@app.route('/Reclusos/<int:idRecluso>', methods=['GET'])
def get_recluso(idRecluso):
    recluso = next((r for r in reclusos_data if r["id_recluso"] == idRecluso), None)
    if not recluso:
        abort(404, description="Recluso not found")
    return jsonify(recluso)

# Esta app es solo para probar si funciona bien el tema de los acentos
@app.route('/test', methods=['GET'])
def test_encoding():
    data = {"name": "Martínez Ramírez"}
    response = Response(json.dumps(data, ensure_ascii=False), content_type="application/json; charset=utf-8")
    return response

if __name__ == '__main__':
    app.run(debug=True)

""""
Ejemplo de como probar la aplicacion

http://127.0.0.1:5000/Reclusos/5

"""