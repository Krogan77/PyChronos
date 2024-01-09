

""" class MainWindow """


from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QSizePolicy, QHBoxLayout, QListWidget

from src.core.chrono import new_chrono
from utils import update_timer, start_timer


class MainWindow(QMainWindow):
	""" class MainWindow """

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Chrono")
		self.setMinimumSize(240, 120)
		self.resize(240, 450)
		
		self.setup_ui()
		self.setup_connections()
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
		
		self.btn_new = QPushButton("New chrono")
		self.btn_new.setFixedSize(100, 30)
		self.btn_new.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		self.btn_layout.addWidget(self.btn_new)
		
		self.btn_delete = QPushButton("Delete chrono")
		self.btn_delete.setFixedSize(100, 30)
		self.btn_delete.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		self.btn_layout.addWidget(self.btn_delete)
		
		self.lst_chronos = QListWidget()
		self.main_layout.addWidget(self.lst_chronos)
		
		pass
	
	#
	def setup_connections(self):
		""" Défini les connexions entre les widgets. """
		self.btn_new.clicked.connect(lambda: new_chrono(self))
		pass
	
	def init_variables(self):
		""" Initialise les variables. """
		
		self.chronos = []
		
		self.timer = [0, QTimer()]
		self.timer[1].timeout.connect(lambda: update_timer(self))
		start_timer(self, interval=50)
		pass
	
	#
	def default_values(self):
		""" Défini les valeurs par défaut. """
		
		
		
		pass
	
	#
