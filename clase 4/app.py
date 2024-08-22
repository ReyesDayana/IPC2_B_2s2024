import xml.etree.ElementTree as ET
from ListaTienda import ListaTienda
from ListaEnvio import ListaEnvios


Tiendas = ListaTienda()

def menu():
    ruta = ""
    while True:
        print("------------Menu-------------------")
        print("1. Ingresar la ruta del XML")
        print("2. Procesar Archivo")
        print("3. Analizar Datos")
        print("4. Escribir XML")
        print("5. Graficar")
        print("6. Salir")
        eleccion = int(input("Escribe una opcion: "))

        if eleccion == 1:
            ruta = input("Escribe la ruta del XML: ")
            print(f"Ruta ingresada {ruta}")
        elif eleccion == 2:
            ProcesarArchivo(ruta)
            Tiendas.imprimirTiendas()
        elif eleccion == 3:
            pass
        elif eleccion == 4:
           pass
        elif eleccion == 5:
            Tiendas.Graficar()
        elif eleccion == 6:
            print("Saliendo")
            break
        else:
            print("Opcion invalida")

def ProcesarArchivo(ruta):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        tiendas = root.findall('tiendas')
        for tienda in tiendas:
            nombre = tienda.find('tienda').text
            zona = tienda.find('tienda').get('zona')
            envios = tienda.findall('envio')
            lista_envios = ListaEnvios()
            for envio in envios:
                cliente = envio.text
                direccion = envio.get('direccion')
                estado = envio.get('estado')

                lista_envios.AgregarEnvio(cliente, estado, direccion)
            Tiendas.agregarTienda(nombre, zona, lista_envios)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    menu()