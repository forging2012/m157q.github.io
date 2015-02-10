Title: [Course] Intro CompSec Hw1
Date: 2014-12-18 16:51
Author: m157q
Category: Course
Tags: 
Slug: course-intro-compsec-hw1

### Introduction to Computer Security HW1  
  
<!--more-->  
  
  
1. Select a web site.   
    + Use “Wget” or “Teleport Pro” to mirror the site. Look for comments within comment tags. Give screen dumps and explain what you found.  
        + Screen Dumps & Explanations  
            + I've found some hidden targets that not be shown on the home page of <http://www.nctu.edu.tw>. These website probably still working but out of date or have already be deprecated that nobody maintain the website and may have some flaws. Below is the lists.  
            + <http://140.113.71.51>              ![](http://i.imgur.com/CF1pvvG.png)  
            + <http://president.nctu.edu.tw>      ![](http://i.imgur.com/Zz4VpfZ.png)   
            + <http://www.pac.nctu.edu.tw>        ![](http://i.imgur.com/SpHtizA.png)   
            + <http://www.pac.nctu.edu.tw>        ![](http://i.imgur.com/X4XryCo.png)   
            + <http://www.ccs.nctu.edu.tw>        ![](http://i.imgur.com/RtfBn3e.png)   
            + <http://www.itt.nctu.edu.tw>        ![](http://i.imgur.com/qkom2cv.png)   
            + <http://www.ga.nctu.edu.tw>         ![](http://i.imgur.com/hNJcK9m.png)   
            + <http://campus.creativity.edu.tw>   ![](http://i.imgur.com/81aTjGe.png)   
            + <http://apc.iim.nctu.edu.tw>        ![](http://i.imgur.com/9LzVCmX.png)   
            + <http://saofficion.adm.nctu.edu.tw> ![](http://i.imgur.com/oY4mc4b.png)   
    + Use “DirBuster” with a proxy feature through “privoxy” to enumerate hidden files and directories. Screen dump and explain the hidden files and directories you found.  
        + Screen Dumps & Explanations  
            + ![](http://i.imgur.com/xcDZAej.png), ![](http://i.imgur.com/xTgEVsy.png)  
                + Maybe there some something useful in these index.php files.  
2. Lookup “How I met your girlfriend” in the BlackHat 2010 demo to explain, in 0.5 page, how this was done.  
    + Explanations  
> The speaker first study on the session mechanism of the Facebook.    
> He reduced the complexity of breaking session steps by steps.    
> The Entropy had be redurced from the initial 160 bits to only 20 bits!! He kept tracing the source code and hacking it.    
> Then, he used a techical skill called "NAT pinning" to confuse the router at protocol level.    
> After that, he also used the IRC bot, Geoloction via XSS and HTML5 anti-WAF XSS.    
> Combined all these skills and analysized based on those results.    
> Finally, he used the triangle localization to find someone's girlfriend in reality.   
3. Select a person. Use on-line sites for phone book, social network, information, job, photo management, business directory, jigsaw.com, etc. to summarize, with screen dumps and explanations, what information you can get. If your target is not in US nor native English speaker, you might need to use on-line sites different from the textbook.  
    + Screen Dumps & Explanations  
        + Name: Johnny Depp (John Christopher Depp II)  
        + wikipedia: <http://en.wikipedia.org/wiki/Johnny_Depp>  
        + ![](http://i.imgur.com/80xzYks.png) <http://www.peoplesearch.com>  
            + view more need to pay some money  
        + ![](http://i.imgur.com/2EWoBj9.png) <https://www.facebook.com/JohnnyDepOfficial>  
        + ![](http://i.imgur.com/gxOzrxm.png) <http://www.reunion.com/johnnydepp/>  
        + ![](http://i.imgur.com/hZJntIv.png) <http://www.mylife.com/mick563>  
        + ![](http://i.imgur.com/DPK0hac.png) <https://twitter.com/J0HNNYDepp>  
4. Google “XYZ resume firewall” and “XYZ resume intrusion detection” where “XYZ” is the name of your target company.  Screen dump “useful” results and explain what you got.  
    + Screen Dumps & Explanations  
        + ![](http://i.imgur.com/SA9q2OV.png) ![](http://i.imgur.com/Mcd1JPp.png)  
            + A company called "Systems Technology International" is looking for who will use Linux iptables firewall.  
        + ![ICF International](http://i.imgur.com/HKiS7HA.png)  
            + A company called "ICF International" is looking for who have experience with using Snort IDS.  
5. Lookup Archive.org and Google cached results, and select a target web site. Compare the differences between an archived and cached copy with its current on-line web site. Give screen dump and explain the differences.  
    + Screen Dumps & Explanations  
        + Archive.org ![](http://i.imgur.com/x8JBtUx.png)  
            + 2014/02/09  
        + Google cached ![](http://i.imgur.com/SGSu0ac.png)  
            + 2014/04/07 01:16:27 GMT  
        + current ![](http://i.imgur.com/PTNr8NS.png)  
            + 2014/04/07 09:00:03 GMT  
        + Archive.org have older information. Google cached seems no different from the current website because the cached information just few hours ago.  
6. Find Google Hacking Database at hackersforcharity.org/ghdb/. Summarize what it has and select 3 strings to search. Screen dump and explain what you got.  
    + What GHDB has  
        + it store the google search sentences which can be used to search some specific websites vulnerabilities. There are many entries and each entry have many google search sentences for searching vulnerabilities. The information on the GHDB maybe too old. The newest record is almost eight years ago (2006), though it seems still working...  
    + Screen Dumps & Explanation  
        + Juicy information of the websites built by AppServ  
            + ![](http://i.imgur.com/zr7trQ3.png)   
            + ![](http://i.imgur.com/xcOUM7P.png)  
        + .xls files within user id and password  
            + ![](http://i.imgur.com/1wnb0V4.png)  
            + ![](http://i.imgur.com/sPEihyp.png)  
        + backup directories of the server  
            + ![](http://i.imgur.com/Jiylrey.png)  
            + ![](http://i.imgur.com/kf0nwn2.png)  
7. Select a web site. Start from whois.iana.org to find its registry, registrar, and registrant. Also select an IP address. Start from arin.net to find who owns the IP address. Show your screen dump and explain.   
    + Screen Dumps & Explanations  
        + whois.iana.org - www.nctu.edu.tw  
            + ![](http://i.imgur.com/wGE5htx.png)  
            + ![](http://i.imgur.com/ElLprog.png)  
            + Registry: Taiwan Network Information Center (TWNIC)  
            + Registrar: rs.twnic.net.tw  
            + Registrant: Vice CEO  
        + arin.net - 8.8.8.8  
            + ![](http://i.imgur.com/skF0Ihn.png)  
            + 8.8.8.8 is Google DNS Server     
8. Select a domain name. Use nslookup to dump its DNS records. Show your screen dump and explain.  
    + Screen Dumps & Explanations  
        + ![](http://i.imgur.com/WgTP49I.png)   
        + The <http://www.nctu.edu.tw> has three IP for load balancing.  
9. Select a domain name. Use traceroute or similar tools to find the access path to that domain. Show your screen dump and explain.  
    + Screen Dumps & Explanations  
        + ![](http://i.imgur.com/7c4T1Tg.png)  
        + The destination server seems close the ICMP, so traceroute didn't get the 5th hop ICMP "time exceeded" signal.  
10. Follow the case study right before chapter 1. Select one target and run through all tools (Tor, Vidalia, Privoxy, tor-resolve, proxychains, Nmap, socat, nc). Screen dump the process and explain what you got in your screen.  
    + Screen Dumps & Explanations  
        + turn on vidalia ![](http://i.imgur.com/Q0rbdUC.png)  
        + using tor ![](http://i.imgur.com/7Mql36D.png)  
        + finding target ![](http://i.imgur.com/a4OG9VE.png)  
        + found target ![](http://i.imgur.com/8XmUBT5.png)  
        + used tor-resolve to get target ip ![](http://i.imgur.com/R4MRsHc.png)  
        + using proxychains and nmap ![](http://i.imgur.com/AawbaO5.png), ![](http://i.imgur.com/AWg01Ud.png)  
        + using socat ![](http://i.imgur.com/jn5VMPq.png)  
        + get target informations ![](http://i.imgur.com/SZa3IQO.png)  