import inspect 
import logging

class  Logger:
	"""docstring for  Logger"""
	def logobj(self, lvl):
		fname = inspect.stack()[1][3]
		logger = logging.getLogger(fname)
		logger.setLevel(logging.DEBUG)
		console = logging.StreamHandler()
		console.setLevel(lvl)
		frmt = logging.Formatter('%(asctime)s - %(message)s')
		console.setFormatter(frmt)
		logger.addHandler(console)
		return logger
		