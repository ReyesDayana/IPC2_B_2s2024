import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import re

class Diccionario:
    def __init__(self, xml_path):
        self.diccionario = self.cargar_diccionario(xml_path)

    def cargar_diccionario(self, xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()

        diccionario = {}

        for umbral in root.find("diccionario"):
            tipo = umbral.tag
            diccionario[tipo]= {
                "optimo": umbral.find("optimo").text.split(", "),
                "neutro": umbral.find("neutro").text.split(", "),
                "inadecuado": umbral.find("inadecuado").text.split(", ")
            }
        return diccionario
    
    def obtener_diccionario(self):
        return self.diccionario
    

class AnalizadorDeMensajes:
    def __init__(self, diccionario):
        self.diccionario = diccionario
    
    def limpiar_palabras(self, mensaje):
        mensaje_limpio = re.sub(r'[^\w\s]', '', mensaje)
        return mensaje_limpio.lower().split()
    
    def contar_palabras(self, mensaje):
        palabras_optimo = 0
        palabras_neutro = 0
        palabras_inadecuado = 0

        palabras = self.limpiar_palabras(mensaje)
        
        for palabra in palabras:
            for tipo, categoria in self.diccionario.items():
                if palabra in categoria["optimo"]:
                    palabras_optimo += 1
                elif palabra in categoria["neutro"]:
                    palabras_neutro += 1
                elif palabra in categoria["inadecuado"]:
                    palabras_inadecuado += 1
        
        return palabras_optimo, palabras_neutro, palabras_inadecuado

class ProcesadorDeCiudades:
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.diccionario = Diccionario(xml_path).obtener_diccionario()
        self.analizador =  AnalizadorDeMensajes(self.diccionario)
        self.resultado = ET.Element("resultado_monitoreo")
        self.fecha = ET.SubElement(self.resultado, "fecha")
        self.fecha.text = "2024-10-10"

    def procesar_ciudades(self):

        tree =  ET.parse(self.xml_path)
        root = tree.getroot()

        for ciudad in root.findall("ciudades/ciudad"):
            nombre_ciudad = ciudad.attrib['nombre']
            ciudad_elem =  ET.SubElement(self.resultado, "ciudad", nombre=nombre_ciudad)
            mensajes_resumen = {"optimo": 0, "neutro": 0, "inadecuado": 0}
            detalle_mensajes = ET.SubElement(ciudad_elem, "detalle_mensajes")
            mensajes = ET.SubElement(ciudad_elem, "mensajes")

            mensaje_numero = 1

            for lectura in ciudad.findall("lectura"):
                mensaje_texto = lectura.find("mensaje").text
                fecha_mensaje = lectura.find("fecha").text
                palabras_optimo, palabras_neutro, palabras_inadecuado = self.analizador.contar_palabras(mensaje_texto)

                if palabras_optimo > palabras_inadecuado:
                    mensajes_resumen["optimo"] += 1
                elif palabras_inadecuado > palabras_optimo:
                    mensajes_resumen["inadecuado"] += 1
                else:
                    mensajes_resumen["neutro"] += 1
                
                mensaje_elem = ET.SubElement(detalle_mensajes, "mensaje", numero=str(mensaje_numero))
                mensaje_fecha = ET.SubElement(mensaje_elem, "fecha")
                mensaje_fecha.text =  fecha_mensaje
                ET.SubElement(mensaje_elem, "palabras_optimo").text = str(palabras_optimo)
                ET.SubElement(mensaje_elem, "palabras_neutro").text = str(palabras_neutro)
                ET.SubElement(mensaje_elem, "palabras_inadecuado").text = str(palabras_inadecuado)

                mensaje_numero += 1
            
            ET.SubElement(mensajes, "optimo").text = str(mensajes_resumen["optimo"])
            ET.SubElement(mensajes, "neutro").text = str(mensajes_resumen["neutro"])
            ET.SubElement(mensajes, "inadecuado").text = str(mensajes_resumen["inadecuado"])
            self.guardar_xml("resultado_monitoreo.xml")

    def guardar_xml(self, output_path):
        xml_string = ET.tostring(self.resultado, encoding="utf-8")
        xml_pretty = minidom.parseString(xml_string).toprettyxml(indent="  ")

        # Guardar el XML formateado en el archivo de salida
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(xml_pretty)

        print(f"XML de resultado guardado en {output_path}")