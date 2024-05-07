import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ListaSimplenteLigadaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lista = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lista Simplemente Ligada Demo')
        self.setGeometry(100, 100, 600, 400)

        # Establecer el fondo de la ventana
        self.setStyleSheet("background-color: #162B4E; color: white;")

        descripcion_texto = (
            '<h3 style="color:#1E90FF;">LISTA SIMPLEMENTE LIGADA</h3>'
            '<p style="color:white;">'
            'Una lista simplemente ligada es una colección de nodos donde cada nodo almacena un elemento de datos y una referencia al siguiente nodo en la lista.'
            '</p>'
            '<p style="color:white;">'
            'El primer nodo en la lista se llama "cabeza" y el último nodo tiene una referencia nula (None) al siguiente nodo.'
            '</p>'
            '<p style="color:white;">'
            'Para agregar un elemento a la lista, se crea un nuevo nodo y se enlaza al final de la lista, actualizando la referencia del último nodo.'
            '</p>'
            '<p style="color:white;">'
            'Para eliminar un elemento de la lista, se actualizan las referencias de los nodos adyacentes para "saltar" el nodo que se va a eliminar.'
            '</p>'
        )
        self.descripcion_label = QLabel(descripcion_texto)
        self.descripcion_label.setStyleSheet("color: white;")

        # Añadir imagen desde la ruta especificada
        self.imagen_label = QLabel()
        pixmap = QPixmap('c:/Users/david/AppData/Local/Temp/listaligada.png')
        self.imagen_label.setPixmap(pixmap)
        self.imagen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.lista_label = QLabel('Lista:')
        self.actualizarListaLabel()
        self.lista_label.setStyleSheet("color: white;")

        layout = QVBoxLayout()
        layout.addWidget(self.descripcion_label)
        layout.addWidget(self.imagen_label)
        layout.addWidget(self.insertar_label)
        layout.addWidget(self.insertar_input)
        layout.addWidget(self.insertar_btn)
        layout.addWidget(self.eliminar_btn)
        layout.addWidget(self.buscar_label)
        layout.addWidget(self.buscar_input)
        layout.addWidget(self.buscar_btn)
        layout.addWidget(self.output_text)
        layout.addWidget(self.lista_label)

        self.setLayout(layout)

    def insertarDato(self):
        dato = self.insertar_input.text()
        if dato:
            self.lista.append(dato)
            self.mostrarMensaje(f'Se ha insertado el dato "{dato}" en la lista.')
            self.actualizarListaLabel()
            self.insertar_input.clear()
        else:
            self.mostrarMensaje('Por favor, ingrese un dato.')

    def eliminarDato(self):
        if self.lista:
            item, ok_pressed = QInputDialog.getItem(self, "Eliminar Dato", "Selecciona el dato a eliminar:", self.lista, 0, False)
            if ok_pressed and item:
                self.lista.remove(item)
                self.mostrarMensaje(f'Se ha eliminado el dato "{item}" de la lista.')
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

    def mostrarMensaje(self, mensaje):
        self.output_text.append(mensaje)

    def actualizarListaLabel(self):
        lista_texto = "Lista: " + ", ".join(self.lista)
        self.lista_label.setText(lista_texto)
