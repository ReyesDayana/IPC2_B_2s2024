from xml.dom.minidom import parse, Document
from libros import biblioteca as librosescribir
def menu():
    ruta = ""
    while True:
        print("------------Menu-------------------")
        print("1. Ingresar la ruta del XML")
        print("2. Imprimir XML")
        print("3. Procesar Archivo")
        print("4. Escribir Archivo")
        print("5. Salir")
        eleccion = int(input("Escribe una opcion: "))

        if eleccion == 1:
            ruta = input("Escribe la ruta del XML: ")
            print(f"Ruta ingresada {ruta}")
        elif eleccion == 2:
            try:
                dom_tree = parse(ruta)
                xmlaimprimir = dom_tree.toprettyxml(indent="  ")
                print(xmlaimprimir)
            except Exception as e:
                print(f"Error al imprimir el XML: {e}")
        elif eleccion == 3:
            analizarArchivo(ruta)
        elif eleccion == 4:
            escribirArchivo()
        elif eleccion == 5:
            print("Saliendo")
            break
        else:
            print("Opcion invalida")


def analizarArchivo(ruta):
    try:
        dom_tree = parse(ruta)
        documentoLibros = dom_tree.documentElement
        libros = documentoLibros.getElementsByTagName("book")
        for libro in libros:
            titulo = libro.getAttribute("title")
            autor = libro.getAttribute("author")
            print(f"--------------Titulo: {titulo} -- Autor: {autor}-----------")
            capitulos = libro.getElementsByTagName("Chapter")
            for capitulo in capitulos:
                nombre = capitulo.firstChild.nodeValue
                pagina = capitulo.getAttribute("page")
                print(f"\tNombre del capitulo: {nombre} -- Pagina donde inicia: {pagina}")
    except Exception as e:
        print(f"Error en el archivo: {e}")

def escribirArchivo():
    documentosalida = Document()
    books = documentosalida.createElement("books")
    documentosalida.appendChild(books)
    for libro in librosescribir['books']:
        book = documentosalida.createElement("book")
        book.setAttribute('title', libro['title'])
        book.setAttribute('author', libro['author'])
        for capitulo in libro['chapters']:
            nuevocapitulo = documentosalida.createElement('Chapter')
            nuevocapitulo.setAttribute('page', capitulo['page'])
            nuevocapitulo.appendChild(documentosalida.createTextNode(capitulo['title']))
            book.appendChild(nuevocapitulo)
        books.appendChild(book)

    with open("xmlminidom.xml", 'w', encoding="utf-8") as f:
        documentosalida.writexml(f,indent="\t", addindent="\t", newl="\n", encoding="utf-8")


if __name__ == "__main__":
    menu()