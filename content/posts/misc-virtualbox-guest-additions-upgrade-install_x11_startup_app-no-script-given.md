Title: [Misc] VirtualBox Guest additions upgrade: install_x11_startup_app: no script given
Date: 2014-11-10 11:14
Author: m157q
Category: Misc
Tags: virtualbox, Upgrade, GuestAdditions, install_x11_startup_app
Slug: misc-virtualbox-guest-additions-upgrade-install_x11_startup_app-no-script-given

<!--more-->  
  
### Guest OS: Ubuntu 14.04  
  
Remove the following symlinks before you install the new version of the Guest addtions  
  
`# rm /usr/lib/x86_64-linux-gnu/VBoxGuestAdditions`  
`# rm /usr/lib/VBoxGuestAdditions`  
`# rm /usr/share/VBoxGuestAdditions`  
  
# Reference  
+ <http://gallinar.blogspot.tw/2012/07/virtualbox-guest-additions-upgrade.html>  