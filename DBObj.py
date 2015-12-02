import pymongo
from Logger import Logger

class DBObj:
    
    def __init__(self,DBName,CollectionName):
        self.name = DBName
        self.collection = CollectionName
        self.log = Logger()
        

    def printobj(self):
        print "DB name is %s" %self.name
        print "Collection name is %s" %self.collection

    def getCollection(self):
        try:
            self.conn = pymongo.MongoClient()
            self.db = self.conn[self.name]
            self.col = self.db[self.collection]
            logger = self.logfunc(20)
            logger.info("[INFO]    Collection Acquired")
            return self.col

        except:
            logger = self.logfunc(40)
            logger.error("[ERROR]    Could not get Collection!")
            
    def logfunc(self, lvl):
        return self.log.logobj(lvl)
