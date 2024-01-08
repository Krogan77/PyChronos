""" class MainWindow """

import sys
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
	""" class MainWindow """

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Chrono")
		self.resize(400, 300)