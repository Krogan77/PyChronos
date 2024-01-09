""" Contient les widgets personnalisés de l'application. """
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class ChronoWidget(QWidget):
	""" Widget de chrono. """
	
	def __init__(self, chrono, parent=None):
		""" Initialise le widget. """
		
		super().__init__(parent)
		
		self.chrono = chrono
		
		self.par = self.parent()
		
		self.setup_ui()
		self.setup_connections()
	
	def setup_ui(self):
		""" Défini l'interface utilisateur. """
		
		self.main_layout = QHBoxLayout()
		self.setLayout(self.main_layout)
		
		self.lb_title = QLabel(self.chrono.__str__())
		self.main_layout.addWidget(self.lb_title)
		
		self.btn_start = QPushButton("Start")
		self.btn_start.setFixedSize(80, 30)
		self.main_layout.addWidget(self.btn_start)
		pass
	
	#
	
	def setup_connections(self):
		""" Défini les connexions entre les widgets. """
		self.btn_start.clicked.connect(self.chrono.activate)
		pass
	
	#
	
	def check_chrono(self):
		""" Vérifie si le chrono est actif. """
		if self.chrono.start is None:
			return False
		else:
			return True
		
	def refresh(self):
		""" Met à jour le widget. """
		if self.check_chrono():
			self.lb_title.setText(self.chrono.__str__())
		pass