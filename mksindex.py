#this program is to for performing multikeyword search on facebook pages

#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error
import sys
import re
#from porterStemmer import PorterStemmer
from collections import defaultdict
from array import array
import gc
import math

#porter=PorterStemmer()


class CreateIndex:

    def __init__(self):
        self.index=defaultdict(list)    #the inverted index
    def tf(self,word, blob):
	
	
	sb=str(blob)
	sb=sb.lower()
	
#	print sb
	
	print sb
	m=sb.split()
#	print word
	#print len(m)
	tscore=float(m.count(word)) / float(len(m))
#	print m.count(word)
	print tscore
	return tscore

    def n_containing(self,word, bloblist):
	#print word
	#print sum(1 for blob in bloblist if word in blob)
	return sum(1 for blob in bloblist if word in blob)

    def idf(self,word, bloblist):
	#print word
	#print len(bloblist) / (n_containing(word, bloblist))
	m = float(len(bloblist))
	n = float(self.n_containing(word, bloblist))
	idscore= math.log( m/n )
	print idscore
	return idscore


    def tfidf(self,word, blob, bloblist):#function to calculate tf-idf scores
	#print word
	#print tf(word, blob)
	#print idf(word, bloblist)
	return self.tf(word, blob) * self.idf(word, bloblist)
    def getTerms(self, line):
        '''given a stream of text, get the terms from the text'''
        line=line.lower()
        line=re.sub(r'[^a-z0-9 ]',' ',line) #put spaces instead of non-alphanumeric characters
        line=line.split()
        line=[x for x in line if x not in self.sw]  #eliminate the stopwords
        #line=[ porter.stem(word, 0, len(word)-1) for word in line]
        return line



    
    def getStopwords(self):
        '''get stopwords from the stopwords file'''
        f=open(self.stopwordsFile, 'r')
        stopwords=[line.rstrip() for line in f]
        self.sw=dict.fromkeys(stopwords)
        f.close()
        

    def getTerms(self, line):
        '''given a stream of text, get the terms from the text'''
	line=str(line)
        line=line.lower()
        line=re.sub(r'[^a-z0-9 ]',' ',line) #put spaces instead of non-alphanumeric characters
        line=line.split()
        line=[x for x in line if x not in self.sw]  #eliminate the stopwords
        #line=[ porter.stem(word, 0, len(word)-1) for word in line]
        return line


    def parseCollection(self):
        ''' returns the id, title and text of the next page in the collection '''
	global data
	global actualinfo
	global g
        d={}
        d['id']=g+1#pageid.group(1)
        d['title']='hai'
        d['text']=str(data[g])#pagetext.group(1)
	g=g+1
	#print d['text']
	actualinfo.append(d['text'])
        

        return d


    def writeIndexToFile(self):
        '''write the inverted index to the file'''
	print "enter the keyword to search"
	global data
	global dictionary
	ra=0
	b=[]
	r=raw_input()
	word=[]
	inpu=self.getTerms(r)
	

        f=open(self.indexFile, 'w')
        for term in self.index.iterkeys():
	    signal=0
            postinglist=[]
            for p in self.index[term]:
                docID=p[0]
                positions=p[1]
                postinglist.append(':'.join([str(docID) ,','.join(map(str,positions))]))
	    for w in inpu:
		if term==w:
			signal=1
			break
	    if signal==1:#checking weather indexing term is in searching words or not
		print term
		for i in postinglist:
			pageid=re.search('(.*?):',i, re.DOTALL)
			#oc=re.search('(.*?),',i, re.DOTALL)
			k=int(pageid.group(1))
			print k
			score=self.tfidf(term,actualinfo[k-1],actualinfo)
			dictionary[k]=dictionary[k]+score
			
			#oc1=int(oc)
			
			if k not in b:
				b.append(k)
				#print data[k-1]
				#print "tf-idf score of document is", score
				#print '\n'
			
            print >> f, ''.join((term,'|',';'.join(postinglist)))
	
	for i in b:
		print " document NO  : ",i
		print "TF-IDF SCORE  : ",dictionary[i]
		print "MESSAGE       : ",extra[i-1][0]
		print "LINK          : ",extra[i-1][1]
		print "LIKES COUNT   : ",extra[i-1][2]
		print "COMMENTS COUNT: ",extra[i-1][3]
		print "SHARE COUNT   : ",extra[i-1][4]
		print '\n','\n'
	     
           
        f.close()
        

    def getParams(self):#this will take files as input
        '''get the parameters stopwords file, collection file, and the output index file'''
        param=sys.argv
        self.stopwordsFile=param[1]
        self.collectionFile=param[2]
        self.indexFile=param[3]
        

    def createIndex(self):
        '''main of the program, creates the index'''
        self.getParams()
        self.collFile=open(self.collectionFile,'r')
        self.getStopwords()
                
        #bug in python garbage collector!
        #appending to list becomes O(N) instead of O(1) as the size grows if gc is enabled.
        gc.disable()
        global data
	for i in data:
        	pagedict={}
        	pagedict=self.parseCollection()
        	#main loop creating the index
        	if  pagedict != {}:                    
            		lines='\n'.join((pagedict['title'],pagedict['text']))
           	        pageid=int(pagedict['id'])
            		terms=self.getTerms(lines)
            
            #build the index for the current page
            		termdictPage={}
            		for position, term in enumerate(terms):
                		try:
		    #print position
                    			termdictPage[term][1].append(position)
               		        except:
                    			termdictPage[term]=[pageid, array('I',[position])]
            
            #merge the current page index with the main index
            		for termpage, postingpage in termdictPage.iteritems():
                		self.index[termpage].append(postingpage)
	    #for i+1 in data:	
           	#pagedict=self.parseCollection()


        gc.enable()
	global g
	#print g
            
        self.writeIndexToFile()
        
    
if __name__=="__main__":
    actualinfo=[]
    g=0
    conn = mysql.connector.connect(host='localhost',
                               database='test',
                               user='root',
                               password='Bharath@1')
   # if conn.is_connected():
                #print('Connected to MySQL database')
    cursor = conn.cursor()
    command="SELECT message FROM PostSummary"
    cursor.execute(command)
    data=cursor.fetchall()
    command="SELECT message,link,likesCount,commentsCount,shareCount FROM PostSummary"
    cursor.execute(command)
    extra=cursor.fetchall()
    print len(data),len(extra)
    
    dictionary={}
    for i in range(len(data)):
    	dictionary[i+1]=0.0
    c=CreateIndex()
    c.createIndex()
    

