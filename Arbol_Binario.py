import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsSimpleTextItem, QMessageBox, QTextEdit
from PyQt6.QtGui import QColor, QPen

class ArbolBinarioInteractivo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Árbol Binario Interactivo")
        self.setGeometry(100, 100, 800, 600)

        self.arbol = ArbolBinario()
        self.scene = QGraphicsScene()
        self.view = QGraphicsBinaryTree(self.scene)

        self.label = QLabel("Ingresa un valor para el nodo:")
        self.textbox = QLineEdit()
        self.insertar_button = QPushButton("Insertar")
        self.eliminar_button = QPushButton("Eliminar")
        self.buscar_button = QPushButton("Buscar")
        self.salir_button = QPushButton("Salir")
        self.datos_label = QLabel("Datos ingresados:")
        self.arbol_label = QLabel("Árbol Binario:")
        self.definicion_text = (
            "ÁRBOL BINARIO\n\n"
            "Un árbol binario es una estructura de datos jerárquica en la cual cada nodo tiene como máximo dos hijos, "
            '\n\n'
            "conocidos como el hijo izquierdo y el hijo derecho. El nodo superior se conoce como nodo raíz, y los nodos "
            '\n\n'
            "que no tienen hijos se llaman hojas. Los árboles binarios se utilizan en diversas aplicaciones, como la "
            '\n\n'
            "implementación de algoritmos de búsqueda y la organización eficiente de datos."
        )
        self.definicion_label = QLabel(self.definicion_text)

        layout = QVBoxLayout()
        layout.addWidget(self.definicion_label)
        layout.addWidget(self.view)
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.insertar_button)
        layout.addWidget(self.eliminar_button)
        layout.addWidget(self.buscar_button)
        layout.addWidget(self.salir_button)
        layout.addWidget(self.datos_label)
        layout.addWidget(self.arbol_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("background-color: #162B4E; color: white;")

        self.label.setStyleSheet("color: white;")
        self.textbox.setStyleSheet("background-color: white; color: black; border-radius: 5px;")
        self.insertar_button.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.eliminar_button.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.buscar_button.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.salir_button.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.datos_label.setStyleSheet("color: white;")
        self.arbol_label.setStyleSheet("color: white;")

        self.insertar_button.clicked.connect(self.insertar_nodo)
        self.eliminar_button.clicked.connect(self.eliminar_nodo)
        self.buscar_button.clicked.connect(self.buscar_nodo)
        self.salir_button.clicked.connect(self.salir)

    def insertar_nodo(self):
        valor = int(self.textbox.text())
        self.arbol.insertar(valor)
        self.actualizar_arbol()
        self.mostrar_datos()

    def eliminar_nodo(self):
        valor = int(self.textbox.text())
        if self.arbol.eliminar(valor):
            self.mostrar_datos()
            self.actualizar_arbol()
            QMessageBox.information(self, "Eliminación exitosa", f"Se ha eliminado el nodo con valor {valor}.")
        else:
            QMessageBox.warning(self, "Error de eliminación", f"No se encontró ningún nodo con valor {valor}.")

    def buscar_nodo(self):
        valor = int(self.textbox.text())
        if self.arbol.buscar(valor):
            QMessageBox.information(self, "Búsqueda exitosa", f"El nodo con valor {valor} está en el árbol.")
        else:
            QMessageBox.warning(self, "Búsqueda fallida", f"No se encontró ningún nodo con valor {valor}.")

    def mostrar_datos(self):
        datos_str = ", ".join(map(str, self.arbol.datos))
        self.datos_label.setText(f"Datos ingresados: {datos_str}")

    def actualizar_arbol(self):
        self.scene.clear()
        if self.arbol.raiz:
            self.view.dibujar_arbol(self.arbol.raiz, 400, 50, 1)

    def salir(self):
        self.close()


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.datos = []

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        respuesta = QMessageBox.question(None, "Derecha o izquierda", f"¿Quieres que {valor} esté a la derecha o a la izquierda de {nodo_actual.valor}?",
                                         buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if respuesta == QMessageBox.StandardButton.Yes:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        self.datos.append(valor)

    def eliminar(self, valor):
        if not self.raiz:
            return False
        else:
            self.raiz = self._eliminar_recursivo(self.raiz, valor)
            return True

    def _eliminar_recursivo(self, nodo, valor):
        if not nodo:
            return None
        elif valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            else:
                sucesor = self._encontrar_sucesor(nodo.derecha)
                nodo.valor = sucesor.valor
                nodo.derecha = self._eliminar_recursivo(nodo.derecha, sucesor.valor)
        return nodo

    def _encontrar_sucesor(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if not nodo:
            return False
        elif nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)


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

            color_nodo = QColor(255, 255, 255)  
            ellipse = QGraphicsEllipseItem(x - radio, y - radio, radio * 2, radio * 2)
            ellipse.setBrush(color_nodo)
            self.scene().addItem(ellipse)
            text = QGraphicsSimpleTextItem(str(nodo.valor))
            text.setPos(x - 5, y - 5)
            self.scene().addItem(text)

            color_linea = QColor(255, 255, 255)  
            pen = QPen(color_linea)
            pen.setWidth(2)
            self.scene().addLine(x, y + radio, x - nivel_offset + (nivel * espacio_horizontal), y + espacio_vertical, pen)
            self.scene().addLine(x, y + radio, x + nivel_offset - (nivel * espacio_horizontal), y + espacio_vertical, pen)
            self.dibujar_arbol(nodo.izquierda, x - nivel_offset + (nivel * espacio_horizontal), y + espacio_vertical, nivel + 1)
            self.dibujar_arbol(nodo.derecha, x + nivel_offset - (nivel * espacio_horizontal), y + espacio_vertical, nivel + 1)









