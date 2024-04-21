import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGroupBox, QHBoxLayout, QComboBox, QLineEdit

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("¿Qué deseas aprender?")
        self.setGeometry(100, 100, 400, 300)

        self.etiqueta = QLabel("Selecciona una operación:")
        self.boton_pila = QPushButton("Pila")
        self.boton_cola = QPushButton("Cola")
        self.boton_lista_simplemente_ligada = QPushButton("Lista simplemente ligada")
        self.boton_lista_doblemente_ligada = QPushButton("Lista doblemente ligada")
        self.boton_lista_circular_doble = QPushButton("Lista circular doble")
        self.boton_arbol_binario = QPushButton("Árbol binario")
        self.boton_arbol_busqueda = QPushButton("Árbol de búsqueda")

        self.boton_pila.clicked.connect(self.mostrar_opciones_pila)
        self.boton_cola.clicked.connect(self.mostrar_opciones_cola)
        self.boton_lista_simplemente_ligada.clicked.connect(self.mostrar_opciones_lista_simplemente_ligada)
        self.boton_lista_doblemente_ligada.clicked.connect(self.mostrar_opciones_lista_doblemente_ligada)
        self.boton_lista_circular_doble.clicked.connect(self.mostrar_opciones_lista_circular_doble)
        self.boton_arbol_binario.clicked.connect(self.mostrar_opciones_arbol_binario)
        self.boton_arbol_busqueda.clicked.connect(self.mostrar_opciones_arbol_busqueda)

        self.etiqueta_opciones = QLabel("")
        self.boton_ejecutar = QPushButton("Ejecutar")
        self.boton_ejecutar.clicked.connect(self.ejecutar_accion)

        layout_botones = QVBoxLayout()
        layout_botones.addWidget(self.etiqueta)
        layout_botones.addWidget(self.boton_pila)
        layout_botones.addWidget(self.boton_cola)
        layout_botones.addWidget(self.boton_lista_simplemente_ligada)
        layout_botones.addWidget(self.boton_lista_doblemente_ligada)
        layout_botones.addWidget(self.boton_lista_circular_doble)
        layout_botones.addWidget(self.boton_arbol_binario)
        layout_botones.addWidget(self.boton_arbol_busqueda)

        layout = QVBoxLayout()
        layout.addLayout(layout_botones)
        layout.addWidget(self.etiqueta_opciones)
        layout.addWidget(self.boton_ejecutar)

        self.setLayout(layout)

    def mostrar_opciones_pila(self):
        self.etiqueta_opciones.setText("Operaciones disponibles para la Pila:\n"
                                       "- Insertar\n"
                                       "- Eliminar\n"
                                       "- Buscar")

    def mostrar_opciones_cola(self):
        self.etiqueta_opciones.setText("Operaciones disponibles para la Cola:\n"
                                       "- Insertar\n"
                                       "- Eliminar\n"
                                       "- Buscar")

    def mostrar_opciones_lista_simplemente_ligada(self):
        self.etiqueta_opciones.setText("Operaciones disponibles para la Lista simplemente ligada:\n"
                                       "- Insertar inicio\n"
                                       "- Insertar final\n"
                                       "- Eliminar inicio\n"
                                       "- Eliminar final\n"
                                       "- Buscar")

    def mostrar_opciones_lista_doblemente_ligada(self):
        self.etiqueta_opciones.setText("Operaciones disponibles para la Lista doblemente ligada:\n"
                                       "- Insertar inicio\n"
                                       "- Insertar final\n"
                                       "- Insertar posición\n"
                                       "- Eliminar inicio\n"
                                       "- Eliminar final\n"
                                       "- Eliminar posición\n"
                                       "- Buscar")

    def mostrar_opciones_lista_circular_doble(self):
        self.etiqueta_opciones.setText("Operaciones disponibles para la Lista circular doble:\n"
                                       "- Insertar inicio\n"
                                       "- Insertar final\n"
                                       "- Eliminar inicio\n"
                                       "- Eliminar final\n"
                                       "- Buscar")

    def mostrar_opciones_arbol_binario(self):
        self.etiqueta_opciones.setText("Operaciones disponibles para el Árbol binario:\n"
                                       "- Insertar\n"
                                       "- Eliminar\n"
                                       "- Buscar")

    def mostrar_opciones_arbol_busqueda(self):
        self.etiqueta_opciones.setText("Operaciones disponibles para el Árbol de búsqueda:\n"
                                       "- Insertar\n"
                                       "- Eliminar\n"
                                       "- Buscar")

    def ejecutar_accion(self):
        # Aquí iría la lógica para ejecutar la operación seleccionada en la estructura de datos correspondiente
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
