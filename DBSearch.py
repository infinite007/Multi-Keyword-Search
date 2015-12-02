from DBObj import DBObj
import json
from bson.json_util import dumps
from Logger import Logger

class DBSearch:
	def __init__(self,DBName,Collection):
		self.collection = Collection
		self.dbname = DBName
		self.log = Logger()

		
	def search(self,key):
		try:
			obj = DBObj(self.dbname,self.collection)
			col = obj.getCollection()
			logger = self.logfunc(20)
			logger.info("[INFO]    Building query object")

			query = {'$text':{'$search':''}}
			query['$text']['$search'] = key
			logger.info("[INFO]    Executing the query ")
			JSONObj = col.find(query, {'_id': False})
			logger.info("[INFO]    Documents retrieved")
			return JSONObj

		except:
			logger.error("[ERROR]    Failed SEARCH operation")

	def getJSON(self,nonJSON):
		doc = json(nonJSON)
		return doc

	def logfunc(self, lvl):
		return self.log.logobj(lvl)
