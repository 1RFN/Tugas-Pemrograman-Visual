import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

class KonversiSuhuApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.style_normal = """
            padding: 10px; 
            font-size: 14px; 
            border: 1px solid #d3d3d3; 
            border-radius: 4px; 
            background-color: white;
        """
        self.style_hijau = """
            padding: 10px; 
            font-size: 14px; 
            border: 1px solid #4CAF50; 
            border-radius: 4px; 
            background-color: #eaf6ec;
        """
        
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.setFixedSize(400, 350)
        self.setStyleSheet("background-color: #f8f9fa; color: black; font-family: Segoe UI, Arial;")

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        judul = QLabel("KONVERSI SUHU")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet("""
            font-size: 16px; 
            font-weight: bold; 
            padding: 15px; 
            background: #3498db; 
            color: white; 
            border-radius: 5px;
        """)

        label_input = QLabel("Masukkan Suhu (Celsius):")
        label_input.setStyleSheet("font-size: 13px;")
        
        self.input_suhu = QLineEdit()
        self.input_suhu.setStyleSheet(self.style_normal) 

        btn_layout = QHBoxLayout()
        self.btn_fahrenheit = QPushButton("Fahrenheit")
        self.btn_kelvin = QPushButton("Kelvin")
        self.btn_reamur = QPushButton("Reamur")

        btn_style = """
            padding: 12px; 
            font-size: 13px; 
            background: #3498db; 
            color: white; 
            border: none; 
            border-radius: 5px;
        """
        
        for btn in [self.btn_fahrenheit, self.btn_kelvin, self.btn_reamur]:
            btn.setStyleSheet(btn_style)
            btn_layout.addWidget(btn)

        self.btn_fahrenheit.clicked.connect(self.hitung_fahrenheit)
        self.btn_kelvin.clicked.connect(self.hitung_kelvin)
        self.btn_reamur.clicked.connect(self.hitung_reamur)

        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True)

        main_layout.addWidget(judul)
        main_layout.addWidget(label_input)
        main_layout.addWidget(self.input_suhu)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.label_hasil)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def get_celsius(self):
        teks_input = self.input_suhu.text().strip()
        if not teks_input:
            QMessageBox.warning(self, "Input Error", "Kolom suhu tidak boleh kosong!")
            return None
            
        try:
            celsius = float(teks_input)
            return celsius
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Input harus berupa angka!")
            return None

    def tampil_hasil(self, celsius, hasil, satuan):
        self.input_suhu.setStyleSheet(self.style_hijau)
        
        teks = f"<b>Hasil Konversi:</b><br><br>{celsius:g} Celsius = {hasil:.2f} {satuan}"
        self.label_hasil.setText(teks)

        self.label_hasil.setStyleSheet("""
            padding: 15px; 
            background: #d6ebff; 
            border-left: 4px solid #004080; 
            border-radius: 4px; 
            font-size: 13px;
            color: #003366;
        """)

    def hitung_fahrenheit(self):
        c = self.get_celsius()
        if c is not None:
            f = (c * 9 / 5) + 32
            self.tampil_hasil(c, f, "Fahrenheit")

    def hitung_kelvin(self):
        c = self.get_celsius()
        if c is not None:
            k = c + 273.15
            self.tampil_hasil(c, k, "Kelvin")

    def hitung_reamur(self):
        c = self.get_celsius()
        if c is not None:
            r = c * 4 / 5
            self.tampil_hasil(c, r, "Reamur")


app = QApplication(sys.argv)
window = KonversiSuhuApp()
window.show()
sys.exit(app.exec())