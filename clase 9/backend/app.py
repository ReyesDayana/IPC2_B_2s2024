from flask import Flask, request, jsonify
from analisis import ProcesadorDeCiudades
import os

app = Flask(__name__)


# Ruta para enviar el XML y realizar el análisis
@app.route('/analizar', methods=['POST'])
def analizar_xml():
    xml_data = request.form.get('xml')
    if not xml_data:
        return jsonify({'error': 'No se envió ningún XML'}), 400

    # Guardar el XML en una carpeta temporal para procesarlo
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    xml_path = os.path.join('uploads', 'resultado_monitoreo.xml')
    with open(xml_path, 'w', encoding='utf-8') as file:
        file.write(xml_data)

    # Realizar el análisis del XML guardado
    procesador = ProcesadorDeCiudades(xml_path)
    procesador.procesar_ciudades()

    return jsonify({'message': 'XML procesado con éxito'}), 200


# Ruta para devolver el XML procesado
@app.route('/resultado', methods=['GET'])
def obtener_resultado():
    output_path = 'resultado_monitoreo.xml'

    if os.path.exists(output_path):
        # Leer el archivo XML y devolverlo como texto
        with open(output_path, 'r', encoding='utf-8') as f:
            resultado_xml = f.read()
        return app.response_class(resultado_xml, mimetype='application/xml')
    else:
        return jsonify({'error': 'No se encontró el archivo de resultado'}), 404


if __name__ == '__main__':
    # Crear la carpeta de uploads si no existe
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)
