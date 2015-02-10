Title: [Course] Network Security Second Midterm
Date: 2014-12-08 09:56
Author: m157q
Category: Course
Tags: course, NetSec
Slug: course-network-security-second-midterm

Find the answers for the questions I am not sure about.  
  
<!--more-->  
  
### Q: Is it correct that a certificate contains both the public key and private key of a user? Who should sign a certificate? why?  
### A: No, only the public key. The trusted Third Party (usually CA) should sign a certificate in order to let anyone needing this user’s public key can obtain the certificate and verify that it is valid by way of the attached trusted signature.  
![Screen Shot 2014-12-08 at 5.49.41 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/cEUty4TXSYaOAdrEa33J_Screen%20Shot%202014-12-08%20at%205.49.41%20PM.png)  
  
---  
  
### Q: What is 802.11i?  
### A: 802.11i is a standard for wireless local area networks (WLANs) that provides improved encryption for networks that use the popular 802.11a and 802.11b (which includes Wi-Fi standards).  
+ [IEEE 802.11i-2004 - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/IEEE_802.11i-2004)  
+ [What is 802.11i? - Definition from WhatIs.com](http://searchmobilecomputing.techtarget.com/definition/80211i)  
  
![Screen Shot 2014-12-08 at 2.51.40 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/EaNha6WRgKO7QNdeagTS_Screen%20Shot%202014-12-08%20at%202.51.40%20PM.png)  
![Screen Shot 2014-12-08 at 2.51.53 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/Xk9kA4QPSLtHl3jDeZHA_Screen%20Shot%202014-12-08%20at%202.51.53%20PM.png)  
  
---  
  
## IPsec  
Check links below for the detail.  
+ [RFC 4301 - Security Architecture for the Internet Protocol](https://tools.ietf.org/html/rfc4301)  
+ [IPsec - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/IPsec)  
  
---  
  
### Q: In IPsec, explain security association (SA) and who may keep it?  
### A: An SA is a simplex "connection" that affords security services to the traffic carried by it. (RFC-4301 4.1)  
### Both client & server will keep it.  
  
+ [Security association - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Security_association)  
	+ A Security Association (SA) is the establishment of shared security attributes between two network entities to support secure communication.  
  + An SA is a simplex (one-way channel) and logical connection which endorses and provides a secure data connection between the network devices.  
  + An SA is a logical group of security parameters that enable the sharing of information to another entity.  
  
### Q: In IPsec, explain security association database (SAD) and who may keep it?  
### A: In each IPsec implementation, there is a nominal Security Association Database (SAD), in which each entry defines the parameters associated with one SA.  Each SA has an entry in the SAD. (RFC-4301 4.4.2)  
### Both client & server will keep it.  
  
![Screen Shot 2014-12-08 at 5.58.34 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/bYmHGdZsSlyE5RFX7NcQ_Screen%20Shot%202014-12-08%20at%205.58.34%20PM.png)  
  
---  
  
### Q: In IPsec, if ESP and AH support authentication? confidentiality?  
### A: AH support authentication; ESP support authentication and cofidentiality;  
![Screen Shot 2014-12-08 at 4.16.48 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/p0uMLF00R4ikT486YLOb_Screen%20Shot%202014-12-08%20at%204.16.48%20PM.png)  
  
---  
  
### Q: IPsec Modes detail  
### A: Transport mode and Tunnel Mode  
![Screen Shot 2014-12-08 at 4.59.20 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/lmQb3SoWRdffRigTUgAP_Screen%20Shot%202014-12-08%20at%204.59.20%20PM.png)  
![Screen Shot 2014-12-08 at 4.18.41 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/wvw3cvopQrGwk9eeFbAK_Screen%20Shot%202014-12-08%20at%204.18.41%20PM.png)  
![Screen Shot 2014-12-08 at 4.18.49 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/zmt1Q0BpRYC3DohJ0GHi_Screen%20Shot%202014-12-08%20at%204.18.49%20PM.png)  
  
---  
  
### Q: IPsec Header  
### ESP Encryption and Authentication  
![Screen Shot 2014-12-08 at 5.08.06 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/htRorHqRTpS1TXxyG1vB_Screen%20Shot%202014-12-08%20at%205.08.06%20PM.png)  
### ESP Transport mode & Tunnel mode  
![Screen Shot 2014-12-08 at 5.10.28 PM.png](http://user-image.logdown.io/user/5428/blog/5443/post/245565/2xD1u9KBTnyHxwL3A3vc_Screen%20Shot%202014-12-08%20at%205.10.28%20PM.png)  
  