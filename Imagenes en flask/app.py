from flask import Flask, render_template, send_file
import xml.etree.ElementTree as ET
import os
from ListaPersonas import Personas
app = Flask(__name__)

@app.route("/")
def saludo():
    return "Hola mundo!"


@app.route('/grafica')
def generar_grafico():
    lista_personas = Personas()
    
    tree = ET.parse('personas.xml')
    root = tree.getroot()
    
    for persona in root.findall('persona'):
        nombre = persona.find('nombre').text
        edad = persona.find('edad').text
        lista_personas.agregarPersona(nombre, edad)
    lista_personas.Graficar()

    return render_template('grafica.html', image_file='static/personas.jpg')

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
