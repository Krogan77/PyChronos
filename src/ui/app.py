

""" class MainWindow """

import sys
import io

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QSizePolicy, QHBoxLayout, QListWidget

from core.chrono import new_chrono, load, delete, save, name_chrono
from ui.utils import update_timer, start_timer, get_db


# Force l'encodage de la console en utf-8 pour éviter les erreurs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class MainWindow(QMainWindow):
	""" class MainWindow """
	
	def __init__(self):
		super().__init__()
		self.setWindowTitle("PyChronos")
		self.setMinimumSize(250, 160)
		self.resize(250, 450)
		
		print("\n🚀 Application started.\n")
		
		# Création de l'ui
		self.setup_ui()
		self.setup_connections()
		
		# Initialisation des variables et valeurs par défaut
		self.init_variables()
		self.default_values()
	
	#
	def setup_ui(self):
		""" Défini l'interface utilisateur. """
		
		self.central_widget = QWidget()
		self.setCentralWidget(self.central_widget)
		
		self.main_layout = QVBoxLayout()
		self.central_widget.setLayout(self.main_layout)
		
		self.btn_layout = QHBoxLayout()
		self.main_layout.addLayout(self.btn_layout)
		
		self.btn_new = QPushButton("New")
		self.btn_new.setFixedSize(100, 30)
		self.btn_new.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		self.btn_layout.addWidget(self.btn_new)
		
		self.btn_rename = QPushButton("Rename")
		self.btn_rename.setFixedSize(100, 30)
		self.btn_rename.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		self.btn_rename.setEnabled(False)
		self.btn_layout.addWidget(self.btn_rename)
		
		self.lst_chronos = QListWidget()
		self.main_layout.addWidget(self.lst_chronos)
		
		self.btn_delete = QPushButton("Delete")
		self.btn_delete.setFixedHeight(30)
		self.btn_delete.setEnabled(False)
		self.main_layout.addWidget(self.btn_delete)
		pass
	
	#
	def setup_connections(self):
		""" Défini les connexions entre les widgets. """
		self.btn_new.clicked.connect(lambda: new_chrono(self))
		
		self.btn_rename.clicked.connect(lambda: name_chrono(self, rename=True))
		
		self.btn_delete.clicked.connect(lambda: delete(self))
		pass
	
	def init_variables(self):
		""" Initialise les variables. """
		
		# Stock les chronos pour un accès plus direct
		self.chronos = []
		
		# Récupère la base de données
		self.db = get_db()
		print("✅ Database loaded.\n")
		
		# Timer servant à mettre à jour l'affichage des chronos continuellement
		self.timer = [0, QTimer()]
		self.timer[1].timeout.connect(lambda: update_timer(self))
		start_timer(self, interval=50)
		print("✅ Timer started.\n")
		pass
	
	#
	def default_values(self):
		""" Défini les valeurs par défaut. """
		load(self)
		pass
	
	#
	def save_chrono(self, chrono):
		""" Sauvegarde le chrono dans la base de données. """
		save(self, chrono)
		
	def closeEvent(self, event):
		""" Définit les actions à effectuer à la fermeture de l'application. """
		print("❌ Close application.\n")
		
	#
