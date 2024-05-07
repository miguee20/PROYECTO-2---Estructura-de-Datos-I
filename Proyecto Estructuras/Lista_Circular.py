import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ListaCircularWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lista = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lista Circular Demo')
        self.setGeometry(100, 100, 600, 400)

        # Establecer el fondo de la ventana
        self.setStyleSheet("background-color: #162B4E; color: white;")

        descripcion_texto = (
            '<h3 style="color:#1E90FF;">LISTA CIRCULAR</h3>'
            '<p style="color:white;">'
            'Una lista circular es similar a una lista enlazada simple, excepto que el último nodo apunta de nuevo al primer nodo en lugar de a None.'
            '</p>'
            '<p style="color:white;">'
            'Esto permite recorrer la lista circularmente, comenzando desde cualquier nodo.'
            '</p>'
            '<p style="color:white;">'
            'La lista circular puede implementarse de manera similar a una lista enlazada simple, pero con la adición de un puntero al primer nodo para permitir un fácil acceso.'
            '</p>'
        )
        self.descripcion_label = QLabel(descripcion_texto)
        self.descripcion_label.setStyleSheet("color: white;")

        # Añadir imagen desde la ruta especificada
        self.imagen_label = QLabel()
        pixmap = QPixmap('c:/Users/david/AppData/Local/Temp/listacircular.png')
        self.imagen_label.setPixmap(pixmap)
        self.imagen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.insertar_inicio_btn = QPushButton('Insertar al inicio')
        self.insertar_inicio_btn.clicked.connect(self.insertarInicio)
        self.insertar_inicio_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.insertar_final_btn = QPushButton('Insertar al final')
        self.insertar_final_btn.clicked.connect(self.insertarFinal)
        self.insertar_final_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.eliminar_inicio_btn = QPushButton('Eliminar al inicio')
        self.eliminar_inicio_btn.clicked.connect(self.eliminarInicio)
        self.eliminar_inicio_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.eliminar_final_btn = QPushButton('Eliminar al final')
        self.eliminar_final_btn.clicked.connect(self.eliminarFinal)
        self.eliminar_final_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.buscar_label = QLabel('Buscar dato:')
        self.buscar_label.setStyleSheet("color: white;")
        self.buscar_input = QLineEdit()

        self.buscar_btn = QPushButton('Buscar')
        self.buscar_btn.clicked.connect(self.buscarDato)
        self.buscar_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.rotar_izquierda_btn = QPushButton('Rotar a la izquierda')
        self.rotar_izquierda_btn.clicked.connect(self.rotarIzquierda)
        self.rotar_izquierda_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.rotar_derecha_btn = QPushButton('Rotar a la derecha')
        self.rotar_derecha_btn.clicked.connect(self.rotarDerecha)
        self.rotar_derecha_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("background-color: white; color: black; border-radius: 5px;")

        self.lista_label = QLabel('Lista:')
        self.actualizarListaLabel()
        self.lista_label.setStyleSheet("color: white;")

        self.input_label = QLabel('Ingresar dato:')
        self.input_text = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.descripcion_label)
        layout.addWidget(self.imagen_label)
        layout.addWidget(self.insertar_inicio_btn)
        layout.addWidget(self.insertar_final_btn)
        layout.addWidget(self.eliminar_inicio_btn)
        layout.addWidget(self.eliminar_final_btn)
        layout.addWidget(self.buscar_label)
        layout.addWidget(self.buscar_input)
        layout.addWidget(self.buscar_btn)
        layout.addWidget(self.rotar_izquierda_btn)
        layout.addWidget(self.rotar_derecha_btn)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.output_text)
        layout.addWidget(self.lista_label)

        self.setLayout(layout)

    def insertarInicio(self):
        dato = self.input_text.text()
        if dato:
            self.lista.insert(0, dato)
            self.mostrarMensaje(f'Se ha insertado el dato "{dato}" al inicio de la lista.')
            self.actualizarListaLabel()
            self.input_text.clear()
        else:
            self.mostrarMensaje('Por favor, ingrese un dato.')

    def insertarFinal(self):
        dato = self.input_text.text()
        if dato:
            self.lista.append(dato)
            self.mostrarMensaje(f'Se ha insertado el dato "{dato}" al final de la lista.')
            self.actualizarListaLabel()
            self.input_text.clear()
        else:
            self.mostrarMensaje('Por favor, ingrese un dato.')

    def eliminarInicio(self):
        if self.lista:
            dato_eliminado = self.lista.pop(0)
            self.mostrarMensaje(f'Se ha eliminado el dato "{dato_eliminado}" del inicio de la lista.')
            self.actualizarListaLabel()
        else:
            self.mostrarMensaje('La lista está vacía, no se puede eliminar ningún dato.')

    def eliminarFinal(self):
        if self.lista:
            dato_eliminado = self.lista.pop()
            self.mostrarMensaje(f'Se ha eliminado el dato "{dato_eliminado}" del final de la lista.')
            self.actualizarListaLabel()
        else:
            self.mostrarMensaje('La lista está vacía, no se puede eliminar ningún dato.')

    def buscarDato(self):
        dato_buscar = self.buscar_input.text()
        if dato_buscar:
            if dato_buscar in self.lista:
                self.mostrarMensaje(f'El dato "{dato_buscar}" se encuentra en la lista.')
            else:
                self.mostrarMensaje(f'El dato "{dato_buscar}" no se encuentra en la lista.')
        else:
            self.mostrarMensaje('Por favor, ingrese un dato a buscar.')

    def rotarIzquierda(self):
        if self.lista:
            dato_movido = self.lista.pop(0)
            self.lista.append(dato_movido)
            self.mostrarMensaje(f'Se ha rotado la lista a la izquierda.')
            self.actualizarListaLabel()
        else:
            self.mostrarMensaje('La lista está vacía, no se puede rotar.')

    def rotarDerecha(self):
        if self.lista:
            dato_movido = self.lista.pop()
            self.lista.insert(0, dato_movido)
            self.mostrarMensaje(f'Se ha rotado la lista a la derecha.')
            self.actualizarListaLabel()
        else:
            self.mostrarMensaje('La lista está vacía, no se puede rotar.')

    def mostrarMensaje(self, mensaje):
        self.output_text.append(mensaje)

    def actualizarListaLabel(self):
        lista_texto = "Lista: " + ", ".join(self.lista)
        self.lista_label.setText(lista_texto)
