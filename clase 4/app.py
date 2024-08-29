import xml.etree.ElementTree as ET
from ListaTienda import ListaTienda
from ListaEnvio import ListaEnvios
from ListaFinal import ListaFinal

Tiendas = ListaTienda()
Enviar = ListaFinal()
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
            AnalizarDatos()
        elif eleccion == 4:
            EscribirXML()
        elif eleccion == 5:
            Tiendas.Graficar()
            Enviar.GraficarLista()
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

def AnalizarDatos():
    print("-----Analizar Datos-------")
    print(f"------Total de tiendas: {Tiendas.tamanio}")
    auxiliar = Tiendas.cabeza
    while True:
        print(f"----Analizando la tienda: {auxiliar.tienda}")
        aux = auxiliar.envio.cabeza
        for i in range(auxiliar.envio.tamanio):
            encontrado = False
            if Enviar.cabeza is None:
                Enviar.Agregar(auxiliar.tienda, aux.cliente, aux.direccion,1, aux.estado)
            else:
                temp = Enviar.cabeza
                for i in range(Enviar.tamanio):
                    if temp.cliente == aux.cliente and temp.direccion == aux.direccion:
                        temp.ordenes += 1
                        encontrado = True
                    temp = temp.next
                if not encontrado:
                    Enviar.Agregar(auxiliar.tienda, aux.cliente, aux.direccion,1, aux.estado)
            aux = aux.next
        if auxiliar.next == Tiendas.cabeza:
            break
        auxiliar =  auxiliar.next

def EscribirXML():
    escribirxml = "<?xml version='1.0' encoding='utf-8'?>\n"
    escribirxml += "<envios>\n"
    auxiliar = Tiendas.cabeza
    for i in range(Tiendas.tamanio):
        escribirxml += "\t<tiendas>\n"
        aux = Enviar.cabeza
        escribirxml += "\t\t<tienda>" + auxiliar.tienda + "</tienda>\n"
        for j in range(Enviar.tamanio):
            if aux.tienda == auxiliar.tienda:
                escribirxml += "\t\t<envio direccion=\""+aux.direccion+"\" ordenes=\""+str(aux.ordenes)+"\">" + aux.cliente + "</envio>\n"
            aux =aux.next
        auxiliar = auxiliar.next
        escribirxml += "\t</tiendas>\n"
    escribirxml += "</envios>\n"
    with open('salida.xml', 'w', encoding='utf-8') as f:
        f.write(escribirxml)

if __name__ == "__main__":
    menu()