from tfidf import rank
from textblob import TextBlob as tb
from DBSearch import DBSearch 

"""
This class implements the vectorization of the document.

creates a dictionary which has word and its tfidf score as a key value pair. 
"""
class vectorize:
	
	def __init__(self):	
		print 'vectorizer initialized!'
	
	def construct(self):
		doc = DBSearch('foo','col').getAll()
		
		for obj in doc:
			#TODO create a bloblist of doc['message']
