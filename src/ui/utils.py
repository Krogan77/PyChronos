

""" Utils.py / Contient les fonctions utilitaires du projet. """


from src.core.chrono import set_lst_chronos


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

