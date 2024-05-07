import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.cabeza = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lista Doblemente Ligada')
        self.setGeometry(100, 100, 600, 400)

        # Establecer el fondo de la ventana
        self.setStyleSheet("background-color: #162B4E; color: white;")

        descripcion_texto = (
            '<h3 style="color:#1E90FF;">LISTA DOBLEMENTE LIGADA</h3>'
            '<p style="color:white;">'
            'Una lista doblemente ligada es una estructura de datos en la que cada nodo tiene dos enlaces, uno al nodo siguiente y otro al nodo anterior.'
            '</p>'
            '<p style="color:white;">'
            'Esto permite recorrer la lista en ambas direcciones.'
            '</p>'
            '<p style="color:white;">'
            'Las operaciones comunes incluyen inserción (al inicio, al final y por posición), eliminación (al inicio, al final y por posición) y búsqueda de valor.'
            '</p>'
        )
        self.descripcion_label = QLabel(descripcion_texto)
        self.descripcion_label.setStyleSheet("color: white;")

        self.insertar_inicio_btn = QPushButton('Insertar al inicio')
        self.insertar_inicio_btn.clicked.connect(self.insertarInicio)
        self.insertar_inicio_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.insertar_final_btn = QPushButton('Insertar al final')
        self.insertar_final_btn.clicked.connect(self.insertarFinal)
        self.insertar_final_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.insertar_posicion_btn = QPushButton('Insertar por posición')
        self.insertar_posicion_btn.clicked.connect(self.insertarPorPosicion)
        self.insertar_posicion_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.eliminar_inicio_btn = QPushButton('Eliminar al inicio')
        self.eliminar_inicio_btn.clicked.connect(self.eliminarInicio)
        self.eliminar_inicio_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.eliminar_final_btn = QPushButton('Eliminar al final')
        self.eliminar_final_btn.clicked.connect(self.eliminarFinal)
        self.eliminar_final_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.eliminar_posicion_btn = QPushButton('Eliminar por posición')
        self.eliminar_posicion_btn.clicked.connect(self.eliminarPorPosicion)
        self.eliminar_posicion_btn.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

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

        self.input_label = QLabel('Ingresar dato:')
        self.input_text = QLineEdit()

        self.posicion_label = QLabel('Posición:')
        self.posicion_text = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.descripcion_label)
        layout.addWidget(self.insertar_inicio_btn)
        layout.addWidget(self.insertar_final_btn)
        layout.addWidget(self.insertar_posicion_btn)
        layout.addWidget(self.eliminar_inicio_btn)
        layout.addWidget(self.eliminar_final_btn)
        layout.addWidget(self.eliminar_posicion_btn)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.posicion_label)
        layout.addWidget(self.posicion_text)
        layout.addWidget(self.buscar_label)
        layout.addWidget(self.buscar_input)
        layout.addWidget(self.buscar_btn)
        layout.addWidget(self.output_text)
        layout.addWidget(self.lista_label)

        self.setLayout(layout)

    def insertarInicio(self):
        dato = self.input_text.text()
        if dato:
            nuevo_nodo = NodoDoble(dato)
            if not self.cabeza:
                self.cabeza = nuevo_nodo
            else:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo_nodo
                self.cabeza = nuevo_nodo
            self.mostrarMensaje(f'Se ha insertado el dato "{dato}" al inicio de la lista.')
            self.actualizarListaLabel()
            self.input_text.clear()
        else:
            self.mostrarMensaje('Por favor, ingrese un dato.')

    def insertarFinal(self):
        dato = self.input_text.text()
        if dato:
            nuevo_nodo = NodoDoble(dato)
            if not self.cabeza:
                self.cabeza = nuevo_nodo
            else:
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nuevo_nodo
                nuevo_nodo.anterior = actual
            self.mostrarMensaje(f'Se ha insertado el dato "{dato}" al final de la lista.')
            self.actualizarListaLabel()
            self.input_text.clear()
        else:
            self.mostrarMensaje('Por favor, ingrese un dato.')

    def insertarPorPosicion(self):
        dato = self.input_text.text()
        posicion = self.posicion_text.text()
        if dato and posicion.isdigit():
            nuevo_nodo = NodoDoble(dato)
            posicion = int(posicion)
            if posicion == 0:
                self.insertarInicio()
            else:
                actual = self.cabeza
                i = 0
                while actual and i < posicion - 1:
                    actual = actual.siguiente
                    i += 1
                if actual:
                    nuevo_nodo.siguiente = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = nuevo_nodo
                    actual.siguiente = nuevo_nodo
                    nuevo_nodo.anterior = actual
                    self.mostrarMensaje(f'Se ha insertado el dato "{dato}" en la posición {posicion} de la lista.')
                    self.actualizarListaLabel()
                    self.input_text.clear()
                    self.posicion_text.clear()
                else:
                    self.mostrarMensaje('La posición especificada está fuera de rango.')
        else:
            self.mostrarMensaje('Por favor, ingrese un dato y una posición válida.')

    def eliminarInicio(self):
        if self.cabeza:
            dato_eliminado = self.cabeza.dato
            if self.cabeza.siguiente:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
            else:
                self.cabeza = None
            self.mostrarMensaje(f'Se ha eliminado el dato "{dato_eliminado}" del inicio de la lista.')
            self.actualizarListaLabel()
        else:
            self.mostrarMensaje('La lista está vacía, no se puede eliminar ningún dato.')

    def eliminarFinal(self):
        if self.cabeza:
            if not self.cabeza.siguiente:
                dato_eliminado = self.cabeza.dato
                self.cabeza = None
            else:
                actual = self.cabeza
                while actual.siguiente.siguiente:
                    actual = actual.siguiente
                dato_eliminado = actual.siguiente.dato
                actual.siguiente = None
            self.mostrarMensaje(f'Se ha eliminado el dato "{dato_eliminado}" del final de la lista.')
            self.actualizarListaLabel()
        else:
            self.mostrarMensaje('La lista está vacía, no se puede eliminar ningún dato.')

    def eliminarPorPosicion(self):
        posicion = self.posicion_text.text()
        if posicion.isdigit():
            posicion = int(posicion)
            if posicion == 0:
                self.eliminarInicio()
            elif self.cabeza:
                actual = self.cabeza
                i = 0
                while actual and i < posicion:
                    actual = actual.siguiente
                    i += 1
                if actual:
                    dato_eliminado = actual.dato
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior
                    if actual.anterior:
                        actual.anterior.siguiente = actual.siguiente
                    self.mostrarMensaje(f'Se ha eliminado el dato "{dato_eliminado}" de la posición {posicion} de la lista.')
                    self.actualizarListaLabel()
                    self.posicion_text.clear()
                else:
                    self.mostrarMensaje('La posición especificada está fuera de rango.')
            else:
                self.mostrarMensaje('La lista está vacía, no se puede eliminar ningún dato.')
        else:
            self.mostrarMensaje('Por favor, ingrese una posición válida.')

    def buscarDato(self):
        dato_buscar = self.buscar_input.text()
        if dato_buscar:
            actual = self.cabeza
            while actual:
                if actual.dato == dato_buscar:
                    self.mostrarMensaje(f'El dato "{dato_buscar}" se encuentra en la lista.')
                    return
                actual = actual.siguiente
            self.mostrarMensaje(f'El dato "{dato_buscar}" no se encuentra en la lista.')
        else:
            self.mostrarMensaje('Por favor, ingrese un dato a buscar.')

    def mostrarMensaje(self, mensaje):
        self.output_text.append(mensaje)

    def actualizarListaLabel(self):
        lista_texto = "Lista: "
        actual = self.cabeza
        while actual:
            lista_texto += str(actual.dato) + " "
            actual = actual.siguiente
        self.lista_label.setText(lista_texto)