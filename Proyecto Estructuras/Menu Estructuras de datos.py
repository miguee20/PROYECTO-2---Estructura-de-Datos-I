import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from Funcionamiento_pilas import PilaWidget
from Funcionamiento_colas import ColaWidget
from Lista_simplemente_ligada import ListaSimplenteLigadaWidget
from Lista_Circular import ListaCircularWidget
from Lista_doblemente_ligada import ListaDobleWidget
from Lista_doblemente_circular import ListaCircularDobleWidget
from Arbol_Binario import ArbolBinarioInteractivo
from Cargar_archivos import FileUploader
from Arbol_busqueda import ArbolBusquedaInteractivo

class MenuEstructuras(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizador de Estructuras")
        self.setGeometry(100, 100, 400, 300)

        self.setStyleSheet("background-color: #162B4E; color: white;")

        self.titulo = QLabel("¡Bienvenido al Visualizador de Estructuras!")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo.setStyleSheet("font-size: 22px; color: white;")

        self.subtitulo = QLabel("¿Qué deseas aprender?")
        self.subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitulo.setStyleSheet("font-size: 12px; color: white;")

        layout = QVBoxLayout()
        layout.addWidget(self.titulo)
        layout.addWidget(self.subtitulo)

        layout.addSpacing(20)

        botones = [
            ("Pila", self.abrir_pila),
            ("Cola", self.abrir_cola),
            ("Lista simplemente ligada", self.abrir_lista_simpl),
            ("Lista circular", self.abrir_lista_circular),
            ("Lista doblemente ligada", self.abrir_lista_doble),
            ("Lista circular doble", self.abrir_lista_circular_doble),
            ("Árbol binario", self.abrir_arbol_binario),
            ("Árbol de búsqueda", self.abrir_arbol_busqueda),
            ("Subir Archivo", self.subir_archivo),
            ("Salir", self.close)
        ]

        for texto, funcion in botones:
            boton = QPushButton(texto)
            boton.clicked.connect(funcion)
            boton.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
            layout.addWidget(boton)
            layout.addSpacing(10)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    def abrir_pila(self):
        self.pila_widget = PilaWidget()
        self.pila_widget.show()

    def abrir_cola(self):
        self.cola_widget = ColaWidget()
        self.cola_widget.show()

    def abrir_lista_simpl(self):
        self.lista_simpl = ListaSimplenteLigadaWidget()
        self.lista_simpl.show()
        
    def abrir_lista_circular(self):
        self.lista_circular = ListaCircularWidget()
        self.lista_circular.show()
        
    def abrir_lista_doble(self):
        self.lista_doble_ligada = ListaDobleWidget()
        self.lista_doble_ligada.show()

    def abrir_lista_circular_doble(self):
        self.lista_circular_doble = ListaCircularDobleWidget()
        self.lista_circular_doble.show() 

    def abrir_arbol_binario(self):
        self.arbol_binario = ArbolBinarioInteractivo()
        self.arbol_binario.show()
        
    def abrir_arbol_busqueda(self):
        self.arbol_busqueda = ArbolBusquedaInteractivo()
        self.arbol_busqueda.show()

    def subir_archivo(self):
        self.cargar_archivos = FileUploader()
        self.cargar_archivos.show()

def main():
    app = QApplication(sys.argv)
    ventana = MenuEstructuras()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
