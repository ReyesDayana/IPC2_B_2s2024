from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = {}
next_id = 1

@app.route('/', methods=['GET'])
def saludar():
    return jsonify({"saludo": "Hola mundo!"})

@app.route('/cargar', methods=['POST'])
def cargar_usuarios():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron usuarios"}), 400
    
    try:
        for user in data:
            if 'username' in user and 'password' in user:
                usuarios[next_id] = {
                    "id": next_id,
                    "username": user["username"],
                    "password": user["password"]
                }
                next_id += 1
            else:
                return jsonify({"error":"Formato incorrecto de usuario"}), 400
        return jsonify({"mensaje": "Usuarios cargados exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al cargar usuarios: {e}"}), 500

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    if usuarios:
        return jsonify(usuarios)
    else:
        return jsonify({"error": "No hay usuarios cargados"})

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    if 'username' not in datos or 'password' not in datos:
        return jsonify({"error": "Faltan campos"})
    
    username = datos['username']
    password = datos['password']

    for user_id, user_info in usuarios.items():
        if user_info["username"]==username and user_info["password"]==password:
            return jsonify({"mensaje": f"usuario {username} ha iniciado sesion", "id": user_id }), 200
        
    return jsonify({"error": "Credenciales incorrectas"})


if __name__ == '__main__':
    app.run(debug=True)