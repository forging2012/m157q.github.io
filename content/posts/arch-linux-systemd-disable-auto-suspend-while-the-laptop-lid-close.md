Title: [Arch Linux] [Systemd] Disable auto suspend while the laptop lid close
Date: 2013-10-15 05:59
Author: m157q
Category: Arch
Tags: Linux, Laptop, Arch, Systemd
Slug: arch-linux-systemd-disable-auto-suspend-while-the-laptop-lid-close

<!--more-->  
  
1. Use editor to modify the configuration file of the systemd-logind  
`#vim /etc/systemd/logind.conf`  
  
2. Find  
`#HandleLidSwitch=suspend`  
  
3. Uncommnet it and then change it to  
`HandleLidSwitch=ignore`  
  
4. After saving the modification, we need to restart the systemd-logind  
`#systemctl restart systemd-logind`  
  
Now the change should be effective now.  
  
---    
  
Ref:  
[How to disable auto suspend when I close laptop lid?][1]  
  
    
  
  
  
[1]: http://unix.stackexchange.com/questions/52643/how-to-disable-auto-suspend-when-i-close-laptop-lid  