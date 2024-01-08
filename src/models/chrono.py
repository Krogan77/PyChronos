""" Contient la classe Chrono. """

from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Chrono:
	""" **Permet de calculer des durées, possède un nom, une durée totale et peut-être relancée.**
	
	- Utilise l'attribut start pour définir une date de début de session et pouvoir calculer la durée
	  depuis cette date. Cet attribut n'est défini que lorsqu'une session est en cours, ce qui permet de
	  l'utilliser pour vérifier si c'est le cas.
	
	- Lorsqu'une session est en cours, la durée totale du chrono est ajouté à la durée de la session seulement pour
	  être affiché, mais n'est redéfini que lorqu'on termine une session.
	
	- L'attribut duration est converti en dictionnaire pour la sauvegarde et reconstruit ensuite.
	"""
	
	title: str  # Titre du chrono
	start: datetime | None = None  # Heure de début de la session actuelle, permet de calculer les durées.
	duration: timedelta | dict = None  # Durée totale du chrono. Calculer par une propriété.
	
	def __post_init__(self):
		""" Défini les valeurs par défaut. """
		
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
		
		total, actual = self.str_durations()
		
		return f"Chrono{self.title}\ntotal={total}\nActual={actual}"
	
	def str_durations(self):
		""" Retourne un str des durées. """
		
		# Récupère les durées
		total, actual = self.get_duration()
		
		# Formate la durée totale
		total = self.divide_duration(total)
		
		# Si une session est en cours, renvoie le str des deux durées
		if actual:
			actual = self.divide_duration(actual)
			return total, actual
		
		# Sinon, renvoie le str de la durée total
		else:
			return total, None
			
	
	@staticmethod
	def divide_duration(duration: timedelta) -> str:
		""" Formate les durées. """
		# Renvoie un str de la durée demandé.
		
		# Récupère les secondes dans le timedelta.
		total_seconds = int(duration.total_seconds())
		
		# Récupère les heures, les minutes et les secondes
		hours, remainder = divmod(total_seconds, 3600)
		minutes, seconds = divmod(remainder, 60)
		
		# Formate la chaîne avec des heures et des minutes
		return f"{hours}h {minutes:02}m {seconds:02}s"
	
	#
	# -----------------LOGIC SESSION------------------ #
	
	def start_chrono(self):
		""" Défini start à l'heure actuelle pour commencer une session """
		
		# Seulement si start est None, définit start à l'heure actuelle.
		if self.start is None:
			self.start = datetime.now()
		
		# Sinon, erreur.
		else:
			raise Exception(f"⚠️ start is not None !!")
	
	@property
	def get_duration(self) -> (timedelta, timedelta):
		""" Renvoie la durée totale et actuelle si une session est en cours. """
		
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
			raise ValueError(f"⚠️ self.start {type(self.start)} !!")

	def end(self):
		""" Met fin au chrono et retire la date de start. """
		
		if self.start is None:
			raise Exception(f"⚠️ self.start is None !!")
		
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
		
		# Range les données de duration dans un dict pour permettre la sauvegarde.
		self.duration = self.duration_to_dict()
	
	
if __name__ == '__main__':
	
	#
	pass

#

#