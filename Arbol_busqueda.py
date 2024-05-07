import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel,
    QLineEdit, QTextEdit, QMessageBox, QComboBox
)
from PyQt6.QtGui import QColor, QPen
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsSimpleTextItem
from PyQt6.QtCore import QStandardPaths


class ArbolBusquedaInteractivo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Árbol de Búsqueda Interactivo")
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet("background-color: #162B4E; color: white;")

        self.arbol = ArbolBusqueda()
        self.scene = QGraphicsScene()
        self.view = QGraphicsBinaryTree(self.scene)

        self.label_insertar = QLabel("Ingresa un valor para insertar:")
        self.textbox_insertar = QLineEdit()
        self.insertar_button = QPushButton("Insertar")
        self.label_direccion = QLabel("Selecciona la dirección:")
        self.combo_direccion = QComboBox()
        self.combo_direccion.addItems(["Izquierda", "Derecha"])
        self.label_buscar = QLabel("Ingresa un valor para buscar:")
        self.textbox_buscar = QLineEdit()
        self.buscar_button = QPushButton("Buscar")
        self.ruta_label = QLabel("Recorrido de búsqueda:")
        self.ruta_text = QTextEdit()
        self.salir_button = QPushButton("Salir")

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.label_insertar)
        layout.addWidget(self.textbox_insertar)
        layout.addWidget(self.label_direccion)
        layout.addWidget(self.combo_direccion)
        layout.addWidget(self.insertar_button)
        layout.addWidget(self.label_buscar)
        layout.addWidget(self.textbox_buscar)
        layout.addWidget(self.buscar_button)
        layout.addWidget(self.ruta_label)
        layout.addWidget(self.ruta_text)
        layout.addWidget(self.salir_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.insertar_button.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.buscar_button.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.salir_button.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")

        self.ruta_text.setStyleSheet("background-color: white; color: black; border-radius: 5px;")

        self.insertar_button.clicked.connect(self.insertar_nodo)
        self.buscar_button.clicked.connect(self.buscar_nodo)
        self.salir_button.clicked.connect(self.salir)

    def insertar_nodo(self):
        valor = int(self.textbox_insertar.text())
        direccion = self.combo_direccion.currentText()
        self.arbol.insertar(valor, direccion)
        self.actualizar_arbol()

    def buscar_nodo(self):
        valor_texto = self.textbox_buscar.text()
        if valor_texto:
            valor = int(valor_texto)
            try:
                encontrado, ruta = self.arbol.buscar_con_ruta(valor)
                if encontrado:
                    self.ruta_text.setText("\n".join(str(val) for val in ruta))
                else:
                    self.ruta_text.setText("No se encontró el valor en el árbol.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Ocurrió un error al buscar el nodo: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa un valor para buscar.")

    def salir(self):
        self.close()

    def actualizar_arbol(self):
        self.scene.clear()
        if self.arbol.raiz:
            self.view.dibujar_arbol(self.arbol.raiz, 400, 50, 1)


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor, direccion):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz, direccion)

    def _insertar_recursivo(self, valor, nodo_actual, direccion):
        if direccion == "Izquierda":
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda, direccion)
        elif direccion == "Derecha":
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha, direccion)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        elif valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def buscar_con_ruta(self, valor):
        return self._buscar_con_ruta_recursivo(self.raiz, valor, [])

    def _buscar_con_ruta_recursivo(self, nodo, valor, ruta_actual):
        if nodo is None:
            return False, ruta_actual
        ruta_actual.append(nodo.valor)
        if valor == nodo.valor:
            return True, ruta_actual
        elif valor < nodo.valor:
            return self._buscar_con_ruta_recursivo(nodo.izquierda, valor, ruta_actual)
        else:
            return self._buscar_con_ruta_recursivo(nodo.derecha, valor, ruta_actual)


class QGraphicsBinaryTree(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setSceneRect(0, 0, 800, 600)

    def dibujar_arbol(self, nodo, x, y, nivel):
        if nodo:
            radio = 20
            espacio_horizontal = 50
            espacio_vertical = 100
            nivel_offset = 100

            # Dibuja el nodo
            color_nodo = QColor(255, 255, 255)  # Blanco
            ellipse = QGraphicsEllipseItem(x - radio, y - radio, radio * 2, radio * 2)
            ellipse.setBrush(color_nodo)
            self.scene().addItem(ellipse)
            text = QGraphicsSimpleTextItem(str(nodo.valor))
            text.setPos(x - 5, y - 5)
            self.scene().addItem(text)

            # Dibuja las conexiones a los hijos
            color_linea = QColor(0, 0, 0)
            pen = QPen(color_linea)
            pen.setWidth(2)
            if nodo.izquierda:
                self.scene().addLine(x, y + radio, x - nivel_offset + (nivel * espacio_horizontal), y + espacio_vertical, pen)
                self.dibujar_arbol(nodo.izquierda, x - nivel_offset + (nivel * espacio_horizontal), y + espacio_vertical, nivel + 1)
            if nodo.derecha:
                self.scene().addLine(x, y + radio, x + nivel_offset - (nivel * espacio_horizontal), y + espacio_vertical, pen)
                self.dibujar_arbol(nodo.derecha, x + nivel_offset - (nivel * espacio_horizontal), y + espacio_vertical, nivel + 1)




