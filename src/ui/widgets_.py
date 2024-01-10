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
		self.set_default_values()
	
	def setup_ui(self):
		""" Défini l'interface utilisateur. """
		
		self.main_layout = QHBoxLayout()
		self.setLayout(self.main_layout)
		
		self.lb_title = QLabel(self.chrono.__str__())
		self.main_layout.addWidget(self.lb_title)
		
		self.btn_start = QPushButton()
		self.btn_start.setCheckable(True)
		self.btn_start.setFixedSize(60, 30)
		self.main_layout.addWidget(self.btn_start)
	
	def setup_connections(self):
		""" Défini les connexions entre les widgets. """
		self.btn_start.clicked.connect(self.activate_chrono)
		pass
	
	def set_default_values(self):
		""" Défini les valeurs par défaut. """
		
		# Modification du bouton start
		self.set_btn_start(checked=True)
	
	#
	
	def set_btn_start(self, checked: bool = False):
		""" **Modification du bouton start.**
		
		:param checked: Si True, redéfini l'état du bouton start.
		"""
		
		# Vérifie l'état du chrono
		check = self.check_chrono()
		
		# Défini le texte du bouton en fonction de l'état du chrono
		text = "Start" if not check else "Stop"
		self.btn_start.setText(text)
		
		# Si checked est True, défini l'état du bouton comme égale à celui du chrono
		if checked:
			self.btn_start.setChecked(check)
		
	#
	
	def activate_chrono(self):
		""" Démarre ou arrête le chrono. """
		print(f"Chrono '{self.chrono.title}' {'stopped' if self.check_chrono() else 'activated'}.\n")
		
		# Active le chrono et redéfini l'état du bouton
		self.chrono.activate()
		self.set_btn_start()
		
		# Sauvegarde le chrono pour stocker sa date de start
		self.par.save_chrono(self.chrono)
	
	def check_chrono(self):
		""" Vérifie si le chrono est actif. """
		if self.chrono.start is None:
			return False
		else:
			return True
		
	def refresh(self, hard: bool = False):
		""" Met à jour le widget. """
		if self.check_chrono() or hard:
			self.lb_title.setText(self.chrono.__str__())