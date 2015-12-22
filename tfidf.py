import math
from nltk.corpus import stopwords

class rank:

	def __init__(self):
		print 'Instantiated rank object'
		self.stop = stopwords.words('english')

	def tf(self,word,doc):
		if word not in self.stop:
			return math.log(1+float(doc.words.count(word))/len(doc.words))
		else :
			return 0

	def idf(self,word,doc=[]):
		length = len(doc)
		i=0
		if word not in self.stop:
			for d in doc:
				if word in d:
					i+=1
			return math.log(1+length/float(1+i)) 
		else:
			return 0
