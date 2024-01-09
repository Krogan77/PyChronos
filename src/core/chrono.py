

""" Contient les fonctions de gestion de chrono. """
from PySide6.QtWidgets import QListWidgetItem

from src.models.chrono import Chrono
from widgets_ import ChronoWidget


def new_chrono(self):
	""" Crée un nouveau chrono. """
	
	# todo: Demander le nom du chrono à l'utilisateur.
	
	chrono = Chrono("New chrono")
	
	self.chronos.append(chrono)
	print(chrono)
	
	chrono_widget = ChronoWidget(chrono=chrono, parent=self)
	item = QListWidgetItem()
	
	self.lst_chronos.insertItem(0, item)
	self.lst_chronos.setItemWidget(item, chrono_widget)
	item.setSizeHint(chrono_widget.sizeHint())
	pass


def set_lst_chronos(self):
	""" Ajuste la liste des chronos. """
	
	# Récupère chaque item de la liste et utilise sa méthode refresh
	for i in range(self.lst_chronos.count()):
		item = self.lst_chronos.item(i)
		chrono_widget = self.lst_chronos.itemWidget(item)
		chrono_widget.refresh()
	
	pass

