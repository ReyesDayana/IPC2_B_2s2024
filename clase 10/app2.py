from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

usuarios = {}
next_id = 1

@app.route('/', methods=['GET'])
def saludo():
    return "Hola"

@app.route('/cargar', methods=['POST'])
def cargar_usuarios():
    global next_id
    
    #El error fue que me faltaron los parentesis
    data = request.get_json() #<-----

    if not data:
        return jsonify({"error": "No trae el json"})
    
    try:
        for user in data:
            if 'nombre' in user and 'edad' in user:
                usuarios[next_id] = {
                    "id": next_id,
                    "nombre": user['nombre'],
                    "edad": user['edad']
                }
                next_id += 1
            else:
                return jsonify({"ERROR": "Formato incorrecto"}), 400
        return jsonify({"Mensaje": "Usuarios cargados"})
    except Exception as e:
        return jsonify({"Error": f"El error es: {e}"})
    
@app.route('/usuarios', methods = ['GET'])
def lista_usuarios():
    return render_template('usuarios.html', usuarios= usuarios)

@app.route('/usuarios/<int:id>', methods = ['GET'])
def mostrar_usuario(id):
    usuario = usuarios.get(id)
    if usuario:
        return render_template("usuario.html", usuario= usuario)
    else:
        return jsonify({"error": "usuario no encontrado"})


if __name__ == '__main__':
    app.run(debug=True)