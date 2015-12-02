#!/usr/bin/env python
import cgi 

class ui:

	def __init__(self):
		print 'UI obj created'

	def mainpg(self):
		#initial page
		print "Content-type:text/html\r\n\r\n"
		print '<html><head><title>Search</title>'
		print '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">'
		print '</head><body>'
		print '<form role="form" method = "post" action = "PYUI.py">'
		print '<div class ="page-header" style="padding:0px;margin:0px;">'
		print '<h2>Search : </h2></div><br><br><br><div class="container" align="center">'
		print '<input type = "text" name = "search">&nbsp&nbsp<span class="glyphicon glyphicon-search"></span><br><br>'
		print '<input type = "submit" class="btn btn-primary" value = "Search" ></div>'
		print '</body>'
		print '</html>'
		#end of initial page


	def results(self,data,count):
		#prints result page
		print "Content-type:text/html\r\n\r\n"
		print '<html><head><title>Search</title>'
		print '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">'
		print '<meta charset = "utf-8"></head><body style="padding:0px;">'
		print '<div class ="page-header" style="padding:0px;margin:0px;"><div><h1 style="left-padding:20px;">Search Results</h1></div></div>'
		print '<br><br>'
		print '<span class="label label-success">'
		print 'fetched %d documents'%(count)
		print '</span><br><br>'
		print '<div align="right">'
		print '<a href="/search.py" button type="button" class="btn btn-info" href ="search.py">' 
		print '<span class="glyphicon glyphicon-arrow-left"></span> Go back</a></div>'
		print '</div><br>'
		print '<div class="container-fluid">'
		print '<ul class="list-group" style="left-padding:5px;">'
		i=0
		for obj in data:	
			print '<li class="list-group-item">'
			i=i+1
			for key,value in obj.viewitems():
				if type(value)==int:
					print key+' : %d <br>'%(value)
				else:
					print key,' : ',value.encode('utf-8'),'<br>'
				
			
			print '<br><br>'
			print '<button type="button" class="btn btn-info">' 
			print '<span class="glyphicon glyphicon-search" align ="right"></span> see more'
			print '</button>'
			print "</li><br><br>"
			
		print '</ul></div>'
		print '<br><br>',i
		print '<a href="/search.py" button type="button" class="btn btn-info" href ="search.py">' 
		print '<span class="glyphicon glyphicon-arrow-left"></span> Go back'
		print '</a><br><br>'
		print '</body></html>'
		#end of result page

	def notfound(self):
		#empty search results
		print "Content-type:text/html\r\n\r\n"
		print '<html><head><title>Search</title>'
		print '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">'
		print '</head><body>'
		print '<div class ="page-header" style="padding:0px;margin:0px;"><div><h1 style="left-padding:20px;">Search Results</h1></div></div>'
		print '<br><br><br><h2 align="center">Sorry no results found!!!</h2>'
		print '<a href="/search.py" button type="button" class="btn btn-info" href ="search.py" align="center">' 
		print '<span class="glyphicon glyphicon-arrow-left"></span> Go back'
		print '</a><br><br>'
		print '</body></html>'