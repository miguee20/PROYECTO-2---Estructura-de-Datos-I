import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt

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

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Software Educativo")
        self.setGeometry(100, 100, 400, 300)

        self.label_titulo = QLabel("<h1>¿Qué deseas aprender?</h1>")
        self.boton_pila = QPushButton("Pila")
        self.boton_pila.clicked.connect(self.mostrar_ventana_pila)

        layout = QVBoxLayout()
        layout.addWidget(self.label_titulo, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.boton_pila, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def mostrar_ventana_pila(self):
        self.ventana_pila = VentanaPila()
        self.ventana_pila.show()

class VentanaPila(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo interactivo de una Pila")
        self.setGeometry(100, 100, 500, 400)

        self.definicion = QLabel("<h2>Una pila es una estructura de datos lineal que sigue el principio de LIFO (Last In, First Out).</h2>"
                                 "<h2>Esto significa que el último elemento que se inserta es el primero en ser eliminado.</h2>"
                                 "<h2>Las operaciones básicas de una pila son:</h2>"
                                 "<ul>"
                                 "<li>push: inserta un elemento en la parte superior de la pila.</li>"
                                 "<li>pop: elimina y devuelve el elemento en la parte superior de la pila.</li>"
                                 "<li>peek: devuelve el elemento en la parte superior de la pila sin eliminarlo.</li>"
                                 "</ul>"
                                 "<h2>Ingrese un valor en el campo de texto y haga clic en 'Insertar' para agregarlo a la pila.</h2>"
                                 "<h2>Haga clic en 'Eliminar' para eliminar el último elemento de la pila.</h2>"
                                 "<h2>Puede utilizar 'Buscar' para verificar si un elemento está presente en la pila.</h2>")

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
        layout.addWidget(self.definicion)
        layout.addWidget(self.label_accion)
        layout.addWidget(self.input_valor)
        layout.addWidget(self.boton_insertar)
        layout.addWidget(self.boton_eliminar)
        layout.addWidget(self.boton_buscar)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

        self.pila = Pila()

    def insertar_valor(self):
        valor = self.input_valor.text()
        if valor:
            self.pila.push(valor)
            mensaje = f"Se ha insertado el valor '{valor}' en la pila.\n"
            mensaje += f"Orden actual de la pila: {self.pila.items}"
            self.resultado.setText(mensaje)
            self.resultado.setStyleSheet("color: green; font-weight: bold;")
            self.input_valor.clear()
        else:
            self.mostrar_mensaje_error("Por favor ingrese un valor.")

    def eliminar_valor(self):
        valor_eliminado = self.pila.pop()
        if valor_eliminado:
            mensaje = f"{valor_eliminado}\n"
            mensaje += f"Orden actual de la pila: {self.pila.items}"
            self.resultado.setText(mensaje)
            self.resultado.setStyleSheet("color: blue; font-weight: bold;")
        else:
            self.mostrar_mensaje_error("La pila está vacía")

    def buscar_valor(self):
        valor = self.input_valor.text()
        if valor:
            mensaje = self.pila.buscar(valor)
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
