Title: [Misc] Find Malicious Website via Google Safe Browsing Diagnostic API
Date: 2015-01-14 14:23
Author: m157q
Category: Misc
Tags: Security, MaliciousWebsite, SafeBrowsing
Slug: misc-find-malicious-website-via-google-safe-browsing-diagnostic-api

One of my friends need to analyze the websites which are sentenced to be malicious website by the Google (Chrome safe browsing) for one of his security related course homeworks.    
He told me that it's very hard to find such links, so I found this kind of solution for him.    
  
![Screen Shot 2015-01-14 at 10.33.22 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/250029/8VlbcZrrRp6b59m115ZO_Screen%20Shot%202015-01-14%20at%2010.33.22%20PM.png)  
  
<!--more-->  
  
### Use the Google Safe Browsing Diagnostic API  
  
<https://www.google.com/safebrowsing/diagnostic?site=Google.com>  
  
+ Change the value of the `site` to some portal site such as Google, Yahoo, ...  
+ Check the result if it has `Malicious software is hosted on 276 domain(s), including ...` like the following pic  
+ Try those urls to see if Google Safe Browsing diagnose it as malicious urls  
  
![Screen Shot 2015-01-14 at 10.35.20 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/250029/gQOE8aQwQxSxFGFCHc6B_Screen%20Shot%202015-01-14%20at%2010.35.20%20PM.png)  
  
### The result of <http://24corp-shop.com/>  
  
![Screen Shot 2015-01-14 at 10.41.41 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/250029/zLtwvW0bQr25rBucejz2_Screen%20Shot%202015-01-14%20at%2010.41.41%20PM.png)  
  
### NOTICE  
  
Sometimes you won't see the "Security Error" message because the result shows the record in last 90 days.  
When you access the website, the malicious software maybe already be removed from that site.  