

""" Utils.py / Contient les fonctions utilitaires du projet. """


from pathlib import Path

from tinydb import TinyDB

# Chemin du dossier du projet
CUR_DIR = Path(__file__).resolve().parent.parent.parent


def get_db():
	""" Crée et Renvoie la base de données. """
	
	# Crée le dossier data s'il n'existe pas
	data_dir = CUR_DIR / "data"
	data_dir.mkdir(exist_ok=True)
	
	# Crée et renvoie le fichier de sauvegarde
	file = data_dir / "chronos.json"
	if not file.exists():
		file.touch()
	db = TinyDB(file, indent=4)
	return db

#

# -------  TIMERS  -------- #


def start_timer(self, interval: int = 1000):
	""" Démarre le timer. """
	
	self.timer.start(interval)
	pass


def update_timer(self):
	""" Met à jour le timer. """
	from core.chrono import set_lst_chronos
	set_lst_chronos(self)
	pass
