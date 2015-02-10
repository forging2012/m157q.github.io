Title: [Shutter] [ArchLinux] Can't edit pictures while using Shutter 
Date: 2013-06-08 12:42
Author: m157q
Category: Shutter
Tags: 
Slug: shutter-archlinux-cant-edit-pictures-while-using-shutter
Status: draft

  
  
After upgraded my Arch Linux, I just can't edit photos with Shutter while the function of taking screenshots is ok.    
    
So, I google for "shutter can't edit archlinux" and founded this article.    
[http://shutter-project.org/downloads/dependencies/][1]    
The function of editing pics depends on libgoo-canvas-perl    
    
In Arch Linux, we just need to type this in terminal    
    
  
`$ yaourt -S libgoo-canvas-perl`    
to install the package from AUR.    
    
Then the function of editing pics works fine.  
  
[1]: http://shutter-project.org/downloads/dependencies/  
