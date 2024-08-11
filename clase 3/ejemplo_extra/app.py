import xml.etree.ElementTree as ET
from xml.dom.minidom import parse, Document
from lxml import etree


def main_menu():
    ruta = ""
    while True:
        print("-----------Menú Principal----------------------")
        print("1. Ingresar la ruta del XML")
        print("2. Procesar archivo minidom")
        print("3. Procesar Archivo ElementTree")
        print("4. Procesar Archivo XPath")
        print("5. Escribir Archivo minidom")
        print("6. Escribir Archivo ElementTree")
        print("7. Salir")
        choice = int(input("Seleccione una opción: "))

        if choice == 1:
            ruta = input("Ingrese la ruta del archivo XML: ")
            print(f"Ruta ingresada: {ruta}")
        elif choice == 2:
            procesarMinidom(ruta)
        elif choice == 3:
            procesarElementTree(ruta)
        elif choice == 4:
            procesarXPath(ruta)
        elif choice == 5:
            EscribirMinidom()
        elif choice == 6:
            EscribirElementTree()
        elif choice == 7:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


def procesarMinidom(ruta):
    dom_tree = parse(ruta)
    biblioteca = dom_tree.documentElement
    libros = biblioteca.getElementsByTagName('libro')
    # Iterar sobre la lista de libros y mostrar el título y autor
    for libro in libros:
        titulo = libro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
        autor = libro.getElementsByTagName('autor')[0].childNodes[0].nodeValue
        print(f'Título: {titulo}, Autor: {autor}')

    # otra forma:
    titulos = biblioteca.getElementsByTagName('titulo')
    for titulo in titulos:
        libro = titulo.firstChild.nodeValue
        print(f'Título: {libro}')

    precios = biblioteca.getElementsByTagName('precio')
    for precio in precios:
        moneda = precio.getAttribute('moneda')
        print(f'Moneda: {moneda}')

    for precio in precios:
        moneda = precio.attributes['moneda'].value
        print(f'Moneda: {moneda}')

def procesarElementTree(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()

    libros = root.findall('libro')
    for libro in libros:
        titulo = libro.find('titulo').text
        autor = libro.find('autor').text
        precio = libro.find('precio')
        moneda = precio.get('moneda')
        print(f'Título: {titulo}, Autor: {autor}, Precio: {precio.text} ({moneda})')


def procesarXPath(ruta):
    tree = etree.parse(ruta)
    root = tree.getroot()

    titulos = root.xpath('//libro/titulo/text()')
    for titulo in titulos:
        print(f'Título: {titulo}')

    precios = root.xpath('//libro/precio')
    for precio in precios:
        moneda = precio.get('moneda')
        print(f'Moneda: {moneda}')


def EscribirMinidom():
    # Crear un nuevo documento XML
    doc = Document()
    # Crear el elemento raíz
    biblioteca = doc.createElement('biblioteca')
    doc.appendChild(biblioteca)

    # Crear un elemento <libro>
    libro = doc.createElement('libro')
    biblioteca.appendChild(libro)

    # Crear y añadir el elemento <titulo>
    titulo = doc.createElement('titulo')
    titulo.appendChild(doc.createTextNode('1984'))
    libro.appendChild(titulo)

    # Crear y añadir el elemento <autor>
    autor = doc.createElement('autor')
    autor.appendChild(doc.createTextNode('George Orwell'))
    libro.appendChild(autor)

    # Crear y añadir el elemento <genero>
    genero = doc.createElement('genero')
    genero.appendChild(doc.createTextNode('Ficción'))
    libro.appendChild(genero)

    # Crear y añadir el elemento <publicacion>
    publicacion = doc.createElement('publicacion')
    libro.appendChild(publicacion)

    # Añadir <editorial> y <anio> dentro de <publicacion>
    editorial = doc.createElement('editorial')
    editorial.appendChild(doc.createTextNode('Secker & Warburg'))
    publicacion.appendChild(editorial)

    anio = doc.createElement('anio')
    anio.appendChild(doc.createTextNode('1949'))
    publicacion.appendChild(anio)

    # Crear y añadir el elemento <precio> con atributo "moneda"
    precio = doc.createElement('precio')
    precio.setAttribute('moneda', 'USD')
    precio.appendChild(doc.createTextNode('9.99'))
    libro.appendChild(precio)

    # Guardar el documento en un archivo XML
    with open('biblioteca.xml', 'w', encoding='utf-8') as f:
        doc.writexml(f, indent="  ", addindent="  ", newl="\n", encoding='utf-8')


def EscribirElementTree():
    # Crear el elemento raíz <biblioteca>
    biblioteca = ET.Element('biblioteca')

    # Crear un subelemento <libro>
    libro = ET.SubElement(biblioteca, 'libro')

    # Añadir título al libro
    titulo = ET.SubElement(libro, 'titulo')
    titulo.text = '1984'

    # Añadir autor al libro
    autor = ET.SubElement(libro, 'autor')
    autor.text = 'George Orwell'

    # Añadir género al libro
    genero = ET.SubElement(libro, 'genero')
    genero.text = 'Ficción'

    # Añadir publicación al libro
    publicacion = ET.SubElement(libro, 'publicacion')
    editorial = ET.SubElement(publicacion, 'editorial')
    editorial.text = 'Secker & Warburg'
    anio = ET.SubElement(publicacion, 'anio')
    anio.text = '1949'

    # Añadir precio al libro con atributo "moneda"
    precio = ET.SubElement(libro, 'precio')
    precio.set('moneda', 'USD')
    precio.text = '9.99'
    # Convertir el elemento raíz en un objeto ElementTree
    tree = ET.ElementTree(biblioteca)

    # Guardar el árbol en un archivo XML
    # Se abre en modo binario para manejo de encodings
    with open('biblioteca2.xml', 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)


if __name__ == "__main__":
    main_menu()
