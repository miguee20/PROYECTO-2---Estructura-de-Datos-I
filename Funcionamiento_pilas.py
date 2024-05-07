import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog
from PyQt6.QtGui import QPixmap

class PilaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.pila = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pila Demo')
        self.setGeometry(100, 100, 600, 400)

        # Establecer el fondo de la ventana
        self.setStyleSheet("background-color: #162B4E; color: white;")

        descripcion_texto = (
            '<h3 style="color:#1E90FF;">PILA</h3>\n'
            '<p style="color:white;">'
            'Una pila (a veces llamada una “pila push-down”) es una colección ordenada de ítems donde la adición '
            'de nuevos ítems y la eliminación de ítems existentes siempre tienen lugar en el mismo extremo.'
            '</p>\n'
            '<p style="color:white;">'
            'Tal extremo se denomina el “tope” el extremo opuesto se denomina la “base”.'
            '</p>\n'
            '<p style="color:white;">'
            'La base de la pila es significativa ya que los ítems almacenados en la pila que están más cerca de la '
            'base representan aquellos que han permanecido más tiempo en la pila.'
            '</p>\n'
            '<p style="color:white;">'
            'El ítem más recientemente agregado es el que está en la posición que será eliminada primero. Este '
            'principio de ordenamiento a veces se denomina LIFO:'
            '</p>\n'
            '<p style="color:white;">'
            'último en entrar, primero en salir. Éste brinda un ordenamiento basado en el tiempo de permanencia en la colección. Los ítems más nuevos están cerca al '
            'tope y los más viejos están más cerca de la base.'
            '</p>'
        )



        self.descripcion_label = QLabel(descripcion_texto)
        
        self.descripcion_label.setStyleSheet("padding: 10px;")

        self.codigo_label = QLabel()
        pixmap = QPixmap("pila_code.png")
        self.codigo_label.setPixmap(pixmap)
        
        self.insertar_label = QLabel('Insertar dato:')
        self.insertar_input = QLineEdit()
        self.insertar_btn = QPushButton('Insertar')
        self.insertar_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.insertar_btn.clicked.connect(self.insertarDato)

        self.eliminar_btn = QPushButton('Eliminar dato')
        self.eliminar_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.eliminar_btn.clicked.connect(self.eliminarDato)

        self.buscar_label = QLabel('Buscar dato:')
        self.buscar_input = QLineEdit()
        self.buscar_btn = QPushButton('Buscar')
        self.buscar_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.buscar_btn.clicked.connect(self.buscarDato)

        self.output_text = QTextEdit()
        self.output_text.setStyleSheet("background-color: white; color: black; border-radius: 5px;")
        
        self.pila_label = QLabel('Pila:')
        self.actualizarPilaLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.descripcion_label)
        layout.addWidget(self.codigo_label)
        layout.addWidget(self.insertar_label)
        layout.addWidget(self.insertar_input)
        layout.addWidget(self.insertar_btn)
        layout.addWidget(self.eliminar_btn)
        layout.addWidget(self.buscar_label)
        layout.addWidget(self.buscar_input)
        layout.addWidget(self.buscar_btn)
        layout.addWidget(self.output_text)
        layout.addWidget(self.pila_label)

        self.setLayout(layout)

    def insertarDato(self):
        dato = self.insertar_input.text()
        if dato:
            self.pila.append(dato)
            self.mostrarMensaje(f'Se ha insertado el dato "{dato}" en la pila.')
            self.actualizarPilaLabel()
            self.insertar_input.clear()
        else:
            self.mostrarMensaje('Por favor, ingrese un dato.')

    def eliminarDato(self):
        if self.pila:
            item, ok_pressed = QInputDialog.getItem(self, "Eliminar Dato", "Selecciona el dato a eliminar:", self.pila, 0, False)
            if ok_pressed and item:
                self.pila.remove(item)
                self.mostrarMensaje(f'Se ha eliminado el dato "{item}" de la pila.')
                self.actualizarPilaLabel()
        else:
            self.mostrarMensaje('La pila está vacía, no se puede eliminar ningún dato.')

    def buscarDato(self):
        dato_buscar = self.buscar_input.text()
        if dato_buscar:
            if dato_buscar in self.pila:
                self.mostrarMensaje(f'El dato "{dato_buscar}" se encuentra en la pila.')
            else:
                self.mostrarMensaje(f'El dato "{dato_buscar}" no se encuentra en la pila.')
        else:
            self.mostrarMensaje('Por favor, ingrese un dato a buscar.')

    def mostrarMensaje(self, mensaje):
        self.output_text.append(mensaje)

    def actualizarPilaLabel(self):
        pila_texto = "Pila: " + ", ".join(self.pila)
        self.pila_label.setText(pila_texto)
