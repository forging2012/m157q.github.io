Title: Shutter 0.94-2 broken after Perl upgraded to 5.26 on Arch Linux  
Slug: shutter-0-94-2-broken-after-perl-upgraded-to-5-26-on-arch-linux  
Date: 2017-09-15 20:03:20  
Authors: m157q  
Category: Note  
Tags: shutter, Perl  
Summary: Note for the solution to fix this problem  
  
  
### Error Message  
  
```  
$ shutter  
Can't locate Gnome2.pm in @INC (you may need to install the Gnome2 module)  
(@INC contains:  
    /usr/lib/perl5/5.26/site_perl  
    /usr/share/perl5/site_perl  
    /usr/lib/perl5/5.26/vendor_perl  
    /usr/share/perl5/vendor_perl  
    /usr/lib/perl5/5.26/core_perl  
    /usr/share/perl5/core_perl  
) at /usr/bin/shutter line 37.  
BEGIN failed--compilation aborted at /usr/bin/shutter line 37.  
```  
  
---  
  
### Solution  
  
```  
$ yaourt -S gnomecanvas-perl  
$ yaourt -S gnome-vfs-perl  
$ pacman -Qqo '/usr/lib/perl5/vendor_perl' | xargs yaourt -S --noconfirm  
```  
  
---  
  
### Reference  
  
+ [AUR install packages with Perl broken again - Updating - Manjaro](https://forum.manjaro.org/t/aur-install-packages-with-perl-broken-again/30913/9)  
