# Nama: Irfan Jayadi
# NIM: F1D02310011
# Kelas: D

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
)

class FormBiodataApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.style_normal = """
            padding: 8px;
            font-size: 13px;
            border: 1px solid #d3d3d3;
            border-radius: 4px;
            background-color: white;
        """
        self.style_hijau = """
            padding: 8px;
            font-size: 13px;
            border: 1px solid #4CAF50;
            border-radius: 4px;
            background-color: #eaf6ec;
        """
        
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(450, 480)
        self.setStyleSheet("background-color: #f8f9fa; color: black; font-family: Segoe UI, Arial;")

        main_layout = QVBoxLayout()
        main_layout.setSpacing(8)

        label_nama = QLabel("Nama Lengkap:")
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan nama lengkap") 
        self.input_nama.setStyleSheet(self.style_normal)
        
        label_nim = QLabel("NIM:")
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")
        self.input_nim.setStyleSheet(self.style_normal)

        label_kelas = QLabel("Kelas:")
        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Contoh: TI-2A") 
        self.input_kelas.setStyleSheet(self.style_normal)

        label_jenis_kelamin = QLabel("Jenis Kelamin:")
        self.combo_jenis_kelamin = QComboBox()
        self.combo_jenis_kelamin.addItems(["-- Pilih Jenis Kelamin --", "Laki-laki", "Perempuan"])
        self.combo_jenis_kelamin.setStyleSheet(self.style_normal)

        btn_layout = QHBoxLayout()
        
        self.tombol_tampilkan = QPushButton("Tampilkan")
        self.tombol_tampilkan.setStyleSheet("""
            background-color: #3498db;
            color: white;
            padding: 8px 15px;
            border-radius: 4px;
            font-size: 13px;
            border: none;
        """)
        self.tombol_tampilkan.clicked.connect(self.tampilkan_data)

        self.tombol_reset = QPushButton("Reset")
        self.tombol_reset.setStyleSheet("""
            background-color: #95a5a6;
            color: white;
            padding: 8px 15px;
            border-radius: 4px;
            font-size: 13px;
            border: none;
        """)
        self.tombol_reset.clicked.connect(self.reset_data)

        btn_layout.addWidget(self.tombol_tampilkan)
        btn_layout.addWidget(self.tombol_reset)
        btn_layout.addStretch() 

        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True)

        main_layout.addWidget(label_nama)
        main_layout.addWidget(self.input_nama)
        main_layout.addWidget(label_nim)
        main_layout.addWidget(self.input_nim)
        main_layout.addWidget(label_kelas)
        main_layout.addWidget(self.input_kelas)
        main_layout.addWidget(label_jenis_kelamin)
        main_layout.addWidget(self.combo_jenis_kelamin)
        main_layout.addSpacing(10)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.label_hasil)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def tampilkan_data(self):
        nama = self.input_nama.text().strip()
        nim = self.input_nim.text().strip()
        kelas = self.input_kelas.text().strip()
        jenis_kelamin = self.combo_jenis_kelamin.currentText()

        if not nama or not nim or not kelas:
            QMessageBox.warning(self, "Error", "Semua kolom teks harus diisi!")
            return
        
        if self.combo_jenis_kelamin.currentIndex() == 0: 
            QMessageBox.warning(self, "Error", "Silakan pilih jenis kelamin!")
            return

        self.input_nama.setStyleSheet(self.style_hijau)
        self.input_nim.setStyleSheet(self.style_hijau)
        self.input_kelas.setStyleSheet(self.style_hijau)

        teks_hasil = (
            "<b>DATA BIODATA</b><br><br>"
            f"Nama: {nama}<br>"
            f"NIM: {nim}<br>"
            f"Kelas: {kelas}<br>"
            f"Jenis Kelamin: {jenis_kelamin}"
        )

        self.label_hasil.setText(teks_hasil)
        self.label_hasil.setStyleSheet("""
            background-color: #d6ebd9;
            border-left: 4px solid #1c9b3a;
            padding: 15px;
            border-radius: 4px;
            font-size: 13px;
            color: black;
        """)

    def reset_data(self):
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.combo_jenis_kelamin.setCurrentIndex(0) 
        
        self.input_nama.setStyleSheet(self.style_normal)
        self.input_nim.setStyleSheet(self.style_normal)
        self.input_kelas.setStyleSheet(self.style_normal)

        self.label_hasil.clear()
        self.label_hasil.setStyleSheet("")


app = QApplication(sys.argv)
window = FormBiodataApp()
window.show()
sys.exit(app.exec())
