Title: Convert HTML string to XML string with Python  
Slug: convert-html-string-to-xml-string-with-python  
Date: 2016-08-28 00:47:20  
Authors: m157q  
Category: Note  
Tags: Python, Python 2, HTML, XML  
Summary: Just 3 lines of code in Python 2.  
  
  
```Python2  
from HTMLParser import HTMLParser  
from xml.sax.saxutils import escape  
  
xml_str = escape(HTMLParser().unescape(html_str))  
```  
