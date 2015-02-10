Title: [Misc] percol - interactive pipe in shell
Date: 2014-12-04 15:31
Author: m157q
Category: Misc
Tags: 
Slug: misc-percol-interactive-pipe-in-shell

<!--more-->  
  
Just like less + grep (in time) + echo (the result) to me.  
But the instant query filter maybe useful in some cases.  
  
[mooz/percol](https://github.com/mooz/percol) on GitHub  
  
### Installation  
`$ sudo pip2 install percol`  
  
### Examples  
  
+ `$ percol $file`  
+ `$ ps aux | percol`  
+ `$ git checkout $(git branch | percol)`  