Title: [Course] ITC week9 - Hash
Date: 2013-11-22 07:43
Author: m157q
Category: Course
Tags: course, Cryptography
Slug: course-itc-week9-hash

## NCTUCS 2013-Fall Introduction to Cryptography by Professor Rong-Jaye Chen.  
  
<script async class="speakerdeck-embed" data-id="0e07cca035780131a16332f2791d106a" data-ratio="1.41436464088398" src="//speakerdeck.com/assets/embed.js"></script>  
  
[Slides can be found here.](https://speakerdeck.com/m157q/itc-week9-hash)  
  
  
<!--more-->  
  
---  
  
SHA 系列的比較表  
![SHA series](http://i.imgur.com/kUoznGD.jpg)  
  
> Hash 一定要夠快而且夠亂 才不容易被破解  
  
---  
  
![](http://i.imgur.com/IPPfTk2.jpg)  
  
---  
  
### compression function  
一個 Block 1024 bits 加 SHA-512 出來的 512 bits，出來就會變成原本的三倍  
  
---  
  
> Birthday attack 只要 2^32 就可以找到一個 collision  
  
---  
  
+ W0~W79 共 80 個 Rounds  
+ 2012 年 SHA-3 問世  