Title: [Misc] use find, grep, xargs to rename multiple files
Date: 2014-11-10 13:44
Author: m157q
Category: Misc
Tags: find, grep, ShellScript, xargs, mv, rename
Slug: misc-use-find-grep-xargs-to-rename-multiple-files

Recursively find filenames ends up with **.vh** from pwd directory and change their names from \*.vh to \*.vhd  
  
<!--more-->  
  
**This Only works with BSD xargs !!**  
`find |grep .vh$|xargs -I {}.vh mv {}.vh {}.vhd`  
  
# References  
  
+ <http://stackoverflow.com/questions/10212192/how-to-grep-for-a-filename-instead-of-the-contents-of-a-file>  
+ <http://viewsby.wordpress.com/2012/12/04/find-mvrename-with-xargs-example/>  