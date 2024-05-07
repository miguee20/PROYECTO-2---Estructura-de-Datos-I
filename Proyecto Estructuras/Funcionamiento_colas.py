import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt6.QtGui import QPixmap

class ColaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.cola = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cola Demo')
        self.setGeometry(100, 100, 600, 400)

        # Establecer el fondo de la ventana
        self.setStyleSheet("background-color: #162B4E; color: white;")

        descripcion_texto = (
            '<h3 style="color:#1E90FF;">COLA</h3>'
            '<p style="color:white;">'
            'Una cola es una colección ordenada de elementos donde el primer elemento agregado es el primero en ser eliminado.'
            '</p>'
            '<p style="color:white;">'
            'Este principio de ordenamiento a veces se denomina FIFO: primero en entrar, primero en salir.'
            '</p>'
        )

        self.descripcion_label = QLabel(descripcion_texto)
        self.descripcion_label.setStyleSheet("color: white;")

        self.insertar_label = QLabel('Insertar dato:')
        self.insertar_label.setStyleSheet("color: white;")
        self.insertar_input = QLineEdit()
        self.insertar_btn = QPushButton('Insertar')
        self.insertar_btn.clicked.connect(self.insertarDato)
        self.insertar_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.eliminar_btn = QPushButton('Eliminar dato')
        self.eliminar_btn.clicked.connect(self.eliminarDato)
        self.eliminar_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.buscar_label = QLabel('Buscar dato:')
        self.buscar_label.setStyleSheet("color: white;")
        self.buscar_input = QLineEdit()
        self.buscar_btn = QPushButton('Buscar')
        self.buscar_btn.clicked.connect(self.buscarDato)
        self.buscar_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("background-color: white; color: black; border-radius: 5px;")

        self.cola_label = QLabel('Cola:')
        self.actualizarColaLabel()
        self.cola_label.setStyleSheet("color: white;")

        layout = QVBoxLayout()
        layout.addWidget(self.descripcion_label)
        layout.addWidget(self.insertar_label)
        layout.addWidget(self.insertar_input)
        layout.addWidget(self.insertar_btn)
        layout.addWidget(self.eliminar_btn)
        layout.addWidget(self.buscar_label)
        layout.addWidget(self.buscar_input)
        layout.addWidget(self.buscar_btn)
        layout.addWidget(self.output_text)
        layout.addWidget(self.cola_label)

        self.setLayout(layout)

    def insertarDato(self):
        dato = self.insertar_input.text()
        if dato:
            self.cola.append(dato)
            self.mostrarMensaje(f'Se ha insertado el dato "{dato}" en la cola.')
            self.actualizarColaLabel()
            self.insertar_input.clear()
        else:
            self.mostrarMensaje('Por favor, ingrese un dato.')

    def eliminarDato(self):
        if self.cola:
            dato_eliminado = self.cola.pop(0)
            self.mostrarMensaje(f'Se ha eliminado el dato "{dato_eliminado}" de la cola.')
            self.actualizarColaLabel()
        else:
            self.mostrarMensaje('La cola está vacía, no se puede eliminar ningún dato.')

    def buscarDato(self):
        dato_buscar = self.buscar_input.text()
        if dato_buscar:
            if dato_buscar in self.cola:
                self.mostrarMensaje(f'El dato "{dato_buscar}" se encuentra en la cola.')
            else:
                self.mostrarMensaje(f'El dato "{dato_buscar}" no se encuentra en la cola.')
        else:
            self.mostrarMensaje('Por favor, ingrese un dato a buscar.')

    def mostrarMensaje(self, mensaje):
        self.output_text.append(mensaje)

    def actualizarColaLabel(self):
        cola_texto = "Cola: " + ", ".join(self.cola)
        self.cola_label.setText(cola_texto)
