from flask import Flask, render_template
from modules.lista import leer_alumnos

app = Flask(__name__)


@app.route('/')
def lista_alumnos():
    lista = leer_alumnos("alumnos.xml")
    alumnos_html = lista.generar_html_alumnos()
    return render_template("index.html", alumnos= alumnos_html)

@app.route('/alumno/<carnet>')
def mostrar_alumno(carnet):
    lista = leer_alumnos('alumnos.xml')
    alumno = lista.obtener_alumno_por_carnet(carnet)

    if alumno:
        return render_template("alumno.html", nombre=alumno.nombre, carnet=alumno.carnet )
    else:
        return "<h1>Alumno no encontrado</h1>"

if __name__ =='__main__':
    app.run(debug=True)