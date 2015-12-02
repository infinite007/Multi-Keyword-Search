#!/usr/bin/env python
import cgi
import ui 
from DBSearch import DBSearch

x = DBSearch('foo','col')
form = cgi.FieldStorage()
reply = form.getvalue("search")
y = x.search(reply)
cnt = y.count()
u = ui.ui()
if cnt is not 0:
	u.results(y,cnt)
else:
	u.notfound()

