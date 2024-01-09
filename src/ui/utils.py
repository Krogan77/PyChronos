

""" Utils.py / Contient les fonctions utilitaires du projet. """


from pathlib import Path

from tinydb import TinyDB

from core.chrono import set_lst_chronos

# Chemin du dossier du projet
CUR_DIR = Path(__file__).resolve().parent.parent.parent


def get_db():
	""" Crée et renvoie le fichier de sauvegarde """
	file = CUR_DIR / "data" / "chronos.json"
	if not file.exists():
		file.touch()
	db = TinyDB(file, indent=4)
	return db

#

# -------  TIMERS  -------- #


def start_timer(self, interval: int = 1000):
	""" Démarre le timer. """
	
	self.timer[1].start(interval)
	pass


def update_timer(self):
	""" Met à jour le timer. """
	
	self.timer[0] += 1
	
	set_lst_chronos(self)
	pass


def stop_timer(self):
	""" Arrête le timer. """
	
	self.timer[1].stop()
	pass

