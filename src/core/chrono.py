

""" Contient les fonctions de gestion de chrono. """
from PySide6.QtWidgets import QListWidgetItem, QInputDialog, QMessageBox
from tinydb import where

from models.chrono import Chrono
from ui.widgets_ import ChronoWidget


def new_chrono(self, title: str = None):
	""" Crée un nouveau chrono. """
	
	print("  ➡️   Create new chrono:\n")
	
	if title is None:
		# Demande un nom à l'utilisateur
		title = name_chrono(self)
		if not title:
			return
	
	# Crée le chrono
	chrono = Chrono(title)
	
	self.chronos.append(chrono)
	
	# Sauvegarde le chrono
	print("Saving chrono:")
	save(self, chrono)
	
	# Crée l'item et le widget pour la liste
	chrono_widget = ChronoWidget(chrono=chrono, parent=self)
	item = QListWidgetItem()
	
	# Ajoute le chrono dans la liste
	self.lst_chronos.insertItem(0, item)
	self.lst_chronos.setItemWidget(item, chrono_widget)
	item.setSizeHint(chrono_widget.sizeHint())
	
	self.lst_chronos.setCurrentRow(0)
	
	self.btn_delete.setEnabled(True)
	self.btn_rename.setEnabled(True)
	
	print(f"A new chrono ('{title}') as been created.\n")
	pass


def name_chrono(self, rename: bool = False) -> str | None:
	""" **Demande le nom du chrono à l'utilisateur.**
	
	- Effectue les vérifications sur le nom
	"""
	print("Waiting for a name..")
	
	if rename:
		chrono, item, widget = get_chrono(self)
		title = "Rename chrono"
		text = f"Enter a new name for chrono ('{chrono.title}')"
	else:
		chrono, item, widget = None, None, None
		title = "New chrono"
		text = "Enter a name for new chrono"
	
	title, ok = QInputDialog.getText(self, title, text)
	if not ok or not title:
		return
	
	# Vérification des erreurs
	error = ""
	if len(title) > 16:
		error = "⚠️ Name too long ! 16 chars max.\n"
	elif self.db.contains(where("title") == title):
		error = "⚠️ This chronos already exists !\n"
	elif rename and title == chrono.title:
		error = "⚠️ This name is the same as the current one !\n"
	
	if error:
		QMessageBox.information(self, "🛑 Error detected:", error)
		print("🛑 Error detected:", error)
		return
	
	print(f"✅ Name ('{title}') is valid.\n")
	
	if rename:
		# Récupère le chrono sélectionné et le renomme
		self.db.update({'title': title}, where("title") == chrono.title)
		chrono.title = title
		
		# Update l'item de la liste
		widget.refresh(hard=True)
		
		print(f"Chrono ('{chrono.title}') renamed.\n")
		return
	
	return title
	

def set_lst_chronos(self):
	""" Ajuste la liste des chronos. """
	
	# Récupère chaque item de la liste et utilise sa méthode refresh
	for i in range(self.lst_chronos.count()):
		item = self.lst_chronos.item(i)
		chrono_widget = self.lst_chronos.itemWidget(item)
		chrono_widget.refresh()
	pass


def save(self, chrono: Chrono):
	""" Permet de sauvegarder un chrono """
	
	chrono.set_save()
	
	# Vérifie si le chrono existe déjà
	if self.db.contains(where("title") == chrono.title):
		self.db.update(chrono.__dict__, where("title") == chrono.title)
		print(f"Chrono ('{chrono.title}') saved (Updated).\n")
	else:
		self.db.insert(chrono.__dict__)
		print(f"Chrono ('{chrono.title}') saved (Inserted).\n")
		
	# Une fois que le chrono est sauvegardée, on peut reconvertir ses attributs pour utilisation
	chrono.__post_init__()
	pass

	
def load(self):
	""" Charge les chronos existant dans la base de données à l'ouverture de l'application. """
	
	print("📥 Load chronos:")
	
	chronos = self.db.all()
	
	if not chronos:
		print("No chronos found.\nCreate a base chrono.\n")
		new_chrono(self, title="Best Chrono")
		return
	
	self.lst_chronos.clear()
	
	for i, chrono in enumerate(chronos):
		
		chrono = Chrono(**chrono)
		
		print(f"  {i + 1} - {chrono.title}")
		
		self.chronos.append(chrono)
		
		# Crée l'item et le widget pour la liste
		chrono_widget = ChronoWidget(chrono=chrono, parent=self)
		item = QListWidgetItem()
		
		# Ajoute le chrono dans la liste
		self.lst_chronos.insertItem(0, item)
		self.lst_chronos.setItemWidget(item, chrono_widget)
		item.setSizeHint(chrono_widget.sizeHint())
	
	nbr = len(self.chronos)
	print(f"{nbr} chrono{'s' if nbr > 1 else ''} found.\n")
	
	self.btn_delete.setEnabled(True)
	self.btn_rename.setEnabled(True)
	self.lst_chronos.setCurrentRow(0)
		
	pass


def delete(self):
	""" Supprime le chrono sélectionné. """
	
	print("  ❌   Delete chrono:\n")
	
	if not self.chronos:
		self.btn_delete.setEnabled(False)
		self.btn_rename.setEnabled(False)
		return
	
	chrono, item = get_chrono(self)[:2]
	
	# Demande une confirmation à l'utilisateur
	message = f"Are you sure you want to delete the chrono ('{chrono.title}') ?"
	# noinspection PyUnresolvedReferences
	reply = QMessageBox.question(self, "Delete chrono", message, QMessageBox.Yes | QMessageBox.No)
	# noinspection PyUnresolvedReferences
	if not reply == QMessageBox.Yes:
		print("❌ Canceled\n➡️\n")
		return False
	
	# Supprime le chrono de la liste
	self.chronos.remove(chrono)
	
	# Supprime le chrono de la base de données
	self.db.remove(where("title") == chrono.title)
	
	# Supprime l'item de la liste
	self.lst_chronos.takeItem(self.lst_chronos.row(item))
	
	if not self.chronos:
		self.btn_delete.setEnabled(False)
		self.btn_rename.setEnabled(False)
	
	print(f"Chrono ('{chrono.title}') deleted.\n")


def get_chrono(self):
	""" Récupère le widget et le chrono sélectionné. """
	# Récupère l'item sélectionné
	item = self.lst_chronos.currentItem()
	# Récupère le widget de l'item
	chrono_widget = self.lst_chronos.itemWidget(item)
	# Récupère le chrono
	chrono = chrono_widget.chrono
	return chrono, item, chrono_widget

#

#

#

#

#

#

