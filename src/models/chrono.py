

""" Contient la classe Chrono. """

from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Chrono:
	"""
	Decriptions:
	------------
	**Permet de calculer des durées, possède un nom, une durée totale et peut-être relancée.**
	
	- Utilise l'attribut start pour définir une date de début de session et pouvoir calculer la durée
	  depuis cette date. Cet attribut n'est défini que lorsqu'une session est en cours, ce qui permet de
	  l'utilliser pour vérifier si c'est le cas.
	-
	- Lorsqu'une session est en cours, la durée totale du chrono est ajouté à la durée de la session seulement pour
	  être affiché, mais n'est redéfini que lorqu'on termine une session.
	
	Attributes:
	----------
	- title: str / Titre du chrono.
	
	- start: datetime | str | None = None / Heure de début de la session actuelle, permet de calculer les durées.
	
	- duration: timedelta | dict = None / Durée totale du chrono.
	
	Methods:
	--------
	- __post_init__ / Défini les valeurs par défaut.
	-
	- __str__ / Affichage de l'objet.
	- str_durations / Retourne un str des durées.
	- divide_duration / Formate les durées.
	-
	- activate / Démarre ou arrête le chrono.
	- start_chrono / Défini start à l'heure actuelle pour commencer une session.
	- get_duration / Renvoie la durée totale, et actuelle si une session est en cours.
	- end / Met fin au chrono, redéfini la durée totale et reset start à None.
	-
	- duration_to_dict / Converti un objet timedelta en dictionnaire.
	- reconstruct_duration / Reconstruit l'objet timedelta à partir d'un dictionnaire.
	- set_save / Configure les attributs pour la sauvegarde.

	:return:
	"""
	
	title: str  # Titre du chrono
	start: datetime | str | None = None  # Heure de début de la session actuelle, permet de calculer les durées.
	duration: timedelta | dict = None  # Durée totale du chrono.
	
	def __post_init__(self):
		""" Défini les valeurs par défaut. """
		
		if isinstance(self.start, str):
			self.start = datetime.strptime(self.start, "%c")
		
		# Initialisation de duration s'il n'est pas encore un timedelta
		if self.duration is None:
			self.duration = timedelta()
		
		# Converti les attribut duration str en timedelta si c'est déjà un str
		else:
			self.duration = self.reconstruct_duration()
	
	# -----------------  STR  ----------------------- #
	
	def __str__(self):
		""" Affichage de l'objet """
		# Titre + durée rendu par la méthdoe strg
		# Todo: Ajuster l'affichage en fonction des attributs.
		
		total, actual = self.str_durations()
		
		text_with_actual = f"\nTotal: {total}\nActual: {actual}"
		text_without_actual = f"\nTotal: {total}\n-------"
		
		if actual and actual != total:
			durations = text_with_actual if total != actual else text_without_actual
			return f"⏱️ {self.title.capitalize()}{durations}"
		else:
			return f"⏱️ {self.title.capitalize()}{text_without_actual}"
	
	def str_durations(self):
		""" Retourne un str des durées. """
		
		# Récupère les durées
		total, actual = self.get_duration()
		
		# Formate la durée totale
		total = self.str_duration(total)
		
		# Si une session est en cours, renvoie le str des deux durées
		if actual:
			actual = self.str_duration(actual)
			return total, actual
		
		# Sinon, renvoie le str de la durée totale
		else:
			return total, None
	
	def str_duration(self, duration: timedelta) -> str:
		""" Retourne un str de la durée demandée. """
		
		hours, minutes, seconds = self.divide_duration(duration)
		
		str_ = ""
		str_ += f"{hours}h " if hours else ""
		str_ += f"{minutes:02}m " if minutes else ""
		str_ += f"{seconds:02}s" if hours < 1 else ""
		
		return str_
			
	@staticmethod
	def divide_duration(duration: timedelta) -> tuple:
		""" Divise les durées. """
		# Renvoie un str de la durée demandé.
		
		# Récupère les secondes dans le timedelta.
		total_seconds = int(duration.total_seconds())
		
		# Récupère les heures, les minutes et les secondes
		hours, remainder = divmod(total_seconds, 3600)
		minutes, seconds = divmod(remainder, 60)
		
		# Formate la chaîne avec des heures et des minutes
		return hours, minutes, seconds
	
	#
	# -----------------LOGIC SESSION------------------ #
	
	def activate(self):
		""" Démarre ou arrête le chrono. """
		if self.start is None:
			self.start_chrono()
		else:
			self.end()
	
	def start_chrono(self):
		""" Défini start à l'heure actuelle pour commencer une session """
		
		# Seulement si start est None, définit start à l'heure actuelle.
		if self.start is None:
			self.start = datetime.now()
		
		# Sinon, erreur.
		else:
			raise Exception(f"⚠️ start is not None !!")
	
	def get_duration(self) -> (timedelta, timedelta):
		""" Renvoie la durée totale, et actuelle si une session est en cours. """
		
		# Calcule la durée à l'aide de start et de l'heure actuelle puis la renvoie.
		if isinstance(self.start, datetime):
			now = datetime.now()
			duration = now - self.start
			total_duration = self.duration + duration
			return total_duration, duration
			
		# Si start est None, renvoie la durée totale.
		elif self.start is None:
			return self.duration, None
		else:
			raise ValueError(f"⚠️ >>> type(self.start)\n{type(self.start)}")

	def end(self):
		""" Met fin au chrono, redéfini la durée totale et reset start à None. """
		
		if not isinstance(self.start, datetime):
			raise ValueError(f"⚠️ >>> type(self.start)\n{type(self.start)}")
		
		# Récupère la durée de la session actuelle et recalcule la durée totale.
		self.duration = self.get_duration()[0]
		# Reset start à None
		self.start = None
	
	#
	# ------------------SAVE---------------------- #
	
	def duration_to_dict(self):
		""" Converti un objet timedelta en dictionnaire """
		
		if not isinstance(self.duration, timedelta):
			return
		
		return {
			"days": self.duration.days,
			"seconds": self.duration.seconds,
			"microseconds": self.duration.microseconds
		}
	
	def reconstruct_duration(self):
		""" Reconstruit l'objet timedelta à partir d'un dictionnaire """
		
		# Si duration n'est pas un dict, on le retourne simplement
		if not isinstance(self.duration, dict):
			return self.duration
		
		# Recrée l'objet timedelta
		restored_duration = timedelta(
			days=self.duration["days"],
			seconds=self.duration["seconds"],
			microseconds=self.duration["microseconds"]
		)
		
		# Retourne l'objet timedelta
		return restored_duration
	
	def set_save(self):
		""" Configure les attributs pour la sauvegarde. """
		
		if isinstance(self.start, datetime):
			self.start = self.start.strftime("%c")
		
		# Range les données de duration dans un dict pour permettre la sauvegarde.
		self.duration = self.duration_to_dict()
	
	
if __name__ == '__main__':
	
	#
	pass

#

#