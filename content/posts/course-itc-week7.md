Title: [Course] ITC - week7
Date: 2013-11-06 02:22
Author: m157q
Category: Course
Tags: course, Cryptography
Slug: course-itc-week7

### ITC == Introduction To Cryptography  
  
## Pseudorandom Number Generation And Stream Cipher  
  
<!--more-->  
  
## Algorithm Design  
  
+ Purpose-built algorithms  
    + 專門用來產生 pseudorandom number (bit stream)  
    + 最具代表性: RC4  
+ Algorithms based on existing cryptographic algorithms  
    + Symmetric block ciphers  
    + Asymmetric ciphers  
    + Hash functions and message authentication codes  
  
## Pseudorandom Number Generators  
  
+ Linear Congruential Generators  
  
```mathjax  
X_{n+1} = \left (aX_{n}+c \right ) \mod m  
```  
  
+ Blum Blum Shub Generator (BBS Generator)  
      
## Pseudorandom Number Generation Using A Block Cipher  
  
+ PRNG Using Block Cipher Modes of Operation  
    + CTR Mode           
      ![](http://i.imgur.com/wGzFEX9.png)  
    + OFB Mode            
      ![](http://i.imgur.com/8iDJQdJ.png)            
  
---  
## Stream Ciphers  
  
+ A key is input to a pseudorandom bit generator that produces a stream of 8-bit numbers that are apparently random.  
  
+ The output, called **keystream**, is combined one byte at a time with a plaintext stream using the bitwise XOR operation.  
  
---  
## RC4  
  
+ A stream cipher designed in 1987 by Ron Rivest for RSA security.  