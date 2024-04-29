import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt

# Clase Pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "La pila está vacía"

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "La pila está vacía"

    def buscar(self, elemento):
        if elemento in self.items:
            return f"El elemento '{elemento}' se encuentra en la pila."
        else:
            return f"El elemento '{elemento}' no se encuentra en la pila."

# Clase Cola
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.insert(0, elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "La cola está vacía"

    def buscar(self, elemento):
        if elemento in self.items:
            return f"El elemento '{elemento}' se encuentra en la cola."
        else:
            return f"El elemento '{elemento}' no se encuentra en la cola."

# Clase Nodo y ListaSimplementeLigada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimplementeLigada:
    def __init__(self):
        self.inicio = None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.inicio:
            self.inicio = nuevo_nodo
            return
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_inicio(self):
        if not self.inicio:
            return None
        valor_eliminado = self.inicio.dato
        self.inicio = self.inicio.siguiente
        return valor_eliminado

    def eliminar_final(self):
        if not self.inicio:
            return None
        if not self.inicio.siguiente:
            valor_eliminado = self.inicio.dato
            self.inicio = None
            return valor_eliminado
        actual = self.inicio
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        valor_eliminado = actual.siguiente.dato
        actual.siguiente = None
        return valor_eliminado

    def buscar(self, valor):
        actual = self.inicio
        while actual:
            if actual.dato == valor:
                return f"El elemento '{valor}' se encuentra en la lista."
            actual = actual.siguiente
        return f"El elemento '{valor}' no se encuentra en la lista."

# Clase VentanaPrincipal
class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Software Educativo")
        self.setGeometry(100, 100, 400, 300)

        self.label_titulo = QLabel("<h1 align='center'>¿Qué deseas aprender?</h1>")
        self.boton_pila = QPushButton("Pila")
        self.boton_pila.clicked.connect(self.mostrar_ventana_pila)

        self.boton_cola = QPushButton("Cola")
        self.boton_cola.clicked.connect(self.mostrar_ventana_cola)

        self.boton_lista_simplemente_ligada = QPushButton("Lista simplemente ligada")
        self.boton_lista_simplemente_ligada.clicked.connect(self.mostrar_ventana_lista_simplemente_ligada)

        layout = QVBoxLayout()
        layout.addWidget(self.label_titulo)
        layout.addWidget(self.boton_pila)
        layout.addWidget(self.boton_cola)
        layout.addWidget(self.boton_lista_simplemente_ligada)

        self.setLayout(layout)

    def mostrar_ventana_pila(self):
        self.ventana_pila = VentanaEstructura("Pila", Pila, "https://www.youtube.com/watch?v=9_IOdb9ELRU")
        self.ventana_pila.show()

    def mostrar_ventana_cola(self):
        self.ventana_cola = VentanaEstructura("Cola", Cola, "https://www.youtube.com/watch?v=AH7v7PxSHf8")
        self.ventana_cola.show()

    def mostrar_ventana_lista_simplemente_ligada(self):
        self.ventana_lista_simplemente_ligada = VentanaEstructura("Lista simplemente ligada", ListaSimplementeLigada, "https://www.youtube.com/watch?v=yrl6QR0pYqg")
        self.ventana_lista_simplemente_ligada.show()

# Clase VentanaEstructura
class VentanaEstructura(QWidget):
    def __init__(self, titulo, tipo_estructura, video_link):
        super().__init__()
        self.setWindowTitle(f"Ejemplo interactivo de una {titulo}")
        self.setGeometry(100, 100, 500, 400)

        self.definicion_que_es = QLabel("<h2>¿Qué es?</h2>")
        self.definicion_para_que_sirve = QLabel("<h2>¿Para qué sirve?</h2>")

        if titulo.lower() == "pila":
            self.definicion_que_es_texto = ("<p>Una pila es una estructura de datos lineal que sigue el principio de LIFO (Last In, First Out).</p>"
                                 "<p>Esto significa que el último elemento que se inserta es el primero en ser eliminado.</p>"
                                 "<p>Las pilas son utilizadas en numerosas aplicaciones, como la gestión de tareas en sistemas operativos, manejo de llamadas en una aplicación telefónica, y en la administración de memoria en sistemas informáticos.</p>")
            self.definicion_para_que_sirve_texto = ("<p>Las pilas son útiles cuando se necesita procesar elementos en el mismo orden en que fueron agregados.</p>"
                                                    "<p>Se utilizan comúnmente en la implementación de algoritmos y en la manipulación de datos en aplicaciones informáticas.</p>")
        elif titulo.lower() == "cola":
            self.definicion_que_es_texto = ("<p>Una cola es una estructura de datos lineal que sigue el principio de FIFO (First In, First Out).</p>"
                                 "<p>Esto significa que el primer elemento que se inserta es el primero en ser eliminado.</p>"
                                 "<p>Las colas son utilizadas en numerosas aplicaciones, como la gestión de tareas en sistemas operativos, manejo de solicitudes en servidores, y en la impresión de documentos en colas de impresión.</p>")
            self.definicion_para_que_sirve_texto = ("<p>Las colas son útiles cuando se necesita procesar elementos en el mismo orden en que fueron agregados.</p>"
                                                    "<p>Se utilizan comúnmente en la implementación de algoritmos y en la manipulación de datos en aplicaciones informáticas.</p>")
        elif titulo.lower() == "lista simplemente ligada":
            self.definicion_que_es_texto = ("<p>Una lista simplemente ligada es una estructura de datos enlazada en la que cada nodo apunta al siguiente nodo en la secuencia.</p>"
                                 "<p>Cada nodo contiene un dato y una referencia al siguiente nodo en la lista.</p>"
                                 "<p>Las listas simplemente ligadas son utilizadas en numerosas aplicaciones, como en la implementación de listas enlazadas, gestión de memoria en lenguajes de programación, y en el manejo de estructuras de datos más complejas.</p>")
            self.definicion_para_que_sirve_texto = ("<p>Las listas simplemente ligadas son útiles cuando se necesita una estructura de datos flexible para almacenar una colección de elementos.</p>"
                                                    "<p>Se utilizan comúnmente en la implementación de algoritmos y en la manipulación de datos en aplicaciones informáticas.</p>")

        self.definicion_que_es_label = QLabel(self.definicion_que_es_texto)
        self.definicion_para_que_sirve_label = QLabel(self.definicion_para_que_sirve_texto)

        self.label_video = QLabel(f"<a href='{video_link}'>Ver Video</a>")
        self.label_video.setOpenExternalLinks(True)

        self.label_accion = QLabel("Ingrese un valor:")
        self.input_valor = QLineEdit()

        self.boton_insertar = QPushButton("Insertar")
        self.boton_insertar.clicked.connect(self.insertar_valor)

        self.boton_eliminar = QPushButton("Eliminar")
        self.boton_eliminar.clicked.connect(self.eliminar_valor)

        self.boton_buscar = QPushButton("Buscar")
        self.boton_buscar.clicked.connect(self.buscar_valor)

        self.resultado = QLabel()
        self.resultado.setStyleSheet("color: green; font-weight: bold;")

        layout = QVBoxLayout()
        layout.addWidget(self.definicion_que_es)
        layout.addWidget(self.definicion_que_es_label)
        layout.addWidget(self.definicion_para_que_sirve)
        layout.addWidget(self.definicion_para_que_sirve_label)
        layout.addWidget(self.label_video)
        layout.addWidget(self.label_accion)
        layout.addWidget(self.input_valor)
        layout.addWidget(self.boton_insertar)
        layout.addWidget(self.boton_eliminar)
        layout.addWidget(self.boton_buscar)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

        self.estructura = tipo_estructura()

    def insertar_valor(self):
        valor = self.input_valor.text()
        if valor:
            self.estructura.push(valor)
            mensaje = f"Se ha insertado el valor '{valor}' en la {self.windowTitle().lower()}.\n"
            mensaje += f"Orden actual de la {self.windowTitle().lower()}: {self.estructura.items}"
            self.resultado.setText(mensaje)
            self.resultado.setStyleSheet("color: green; font-weight: bold;")
            self.input_valor.clear()
        else:
            self.mostrar_mensaje_error("Por favor ingrese un valor.")

    def eliminar_valor(self):
        valor_eliminado = self.estructura.pop()
        if valor_eliminado:
            mensaje = f"{valor_eliminado}\n"
            mensaje += f"Orden actual de la {self.windowTitle().lower()}: {self.estructura.items}"
            self.resultado.setText(mensaje)
            self.resultado.setStyleSheet("color: blue; font-weight: bold;")
        else:
            self.mostrar_mensaje_error(f"La {self.windowTitle().lower()} está vacía")

    def buscar_valor(self):
        valor = self.input_valor.text()
        if valor:
            mensaje = self.estructura.buscar(valor)
            self.resultado.setText(mensaje)
            if "encontrado" in mensaje:
                self.resultado.setStyleSheet("color: green; font-weight: bold;")
            else:
                self.resultado.setStyleSheet("color: red; font-weight: bold;")
        else:
            self.mostrar_mensaje_error("Por favor ingrese un valor para buscar.")

    def mostrar_mensaje_error(self, mensaje):
        msg_box = QMessageBox()
        msg_box.setText(mensaje)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Error")
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
