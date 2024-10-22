# Comandos para iniciar el proyecto en django
```bash
django-admin startproject frontend
cd frontend
python manage.py startapp myfrontend
```
# Configurar settings.py:
En el archivo settings.py, agrega la aplicación frontend:
```bash
INSTALLED_APPS = [
    # Otras aplicaciones
    'myfrontend',
]
```
# Pasos para la conexion frontend
1. Crear  vista en Django (en myfrontend/views.py)
2. Crear una plantillas en Django (en myfrontend/templates/index.html)
3. Configurar urls.py en myfrontend
4. configurar urls.py en frontend

La conexion con el backend esta hecha en myfrontend/views.py , en templates estan las plantillas html donde se obtienen la informacion a mandar al backend. Para este ejemplo se manda un json un username y password. Al hacer el request.post se esta comunicando con el servidor en flask y response se iguala a la respuesta que nos da flask (si fue correcta la peticion o si hubo un error). Se hace una de estas con cada uno de los endpoints (de flask) que vamos a estar usando .

```bash
response = requests.post('http://127.0.0.1:5000/api/login', json={
            'username': username,
            'password': password
        })
```
esa direccion es la direccion que les da flask al iniciar el programa + su endpoint (en flask)

# Etiqueta para cargar css en html
Para agregarle css a un archivo html se tiene que poner la etiqueta siguiente (en el html) para que se reconozca que estamos agregando estilo.
```bash
  {% load static %}
```

Ejemplo*:
```bash
   {% load static %}
    <link rel="stylesheet" href="{% static 'styles.css' %}">
```
*El archivo css tiene que estar ubicado en la carpeta static 

# Instrucciones para correr el programa
## Para el backend
1. Abrir una terminal en la carpeta backend (donde se encuentra el archivo app.py)
2. En la terminal correr el comando
```bash
    py app.py
```
## Para el frontend
1. Abrir una terminal en la carpeta frontend (donde es encuentra el archivo manage.py)
2. En la terminal correr el comando
```bash
    python manage.py runserver
```
3. Dirigirse a la direccion
```bash
    http://127.0.0.1:8000/login
```
