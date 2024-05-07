import sys
import os
import shutil
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox, QListWidget
from PyQt6.QtCore import QStandardPaths, QFileInfo


class FileUploader(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Uploader")
        self.setGeometry(100, 100, 400, 300)

        # Establecer el estilo de la ventana principal
        self.setStyleSheet("background-color: #162B4E; color: white;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.btn_upload = QPushButton("Subir Archivo")
        self.btn_upload.clicked.connect(self.upload_file)
        self.btn_upload.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.layout.addWidget(self.btn_upload)

        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("background-color: white; color: black; border-radius: 5px;")
        self.layout.addWidget(self.list_widget)

        self.btn_download = QPushButton("Descargar Archivo")
        self.btn_download.clicked.connect(self.download_file)
        self.btn_download.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 5px;")
        self.layout.addWidget(self.btn_download)

        self.central_widget.setLayout(self.layout)

        self.uploaded_files = []

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", "All Files (*);;Text Files (*.txt)")
        if file_path:
            self.uploaded_files.append(file_path)
            file_name = os.path.basename(file_path)
            self.list_widget.addItem(file_name)
            QMessageBox.information(self, "Éxito", "Archivo subido correctamente.")

    def download_file(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            selected_file_name = selected_item.text()
            selected_file_path = self.uploaded_files[self.list_widget.currentRow()]
            desktop_path = QStandardPaths.standardLocations(QStandardPaths.StandardLocation.DesktopLocation)[0]
            try:
                shutil.copy(selected_file_path, os.path.join(desktop_path, selected_file_name))
                QMessageBox.information(self, "Descargar Archivo", f"Archivo '{selected_file_name}' descargado en el escritorio.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo descargar el archivo: {e}")
        else:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún archivo.")

