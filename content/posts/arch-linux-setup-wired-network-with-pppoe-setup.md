Title: [Arch Linux] Setup wired network with pppoe-setup
Date: 2013-02-20 00:28
Author: m157q
Category: Arch
Tags: pppoe, Linux, Arch, Wired-Network, rp-pppoe
Slug: arch-linux-setup-wired-network-with-pppoe-setup

照著 [ArchWiki - Direct Modem Connection](https://wiki.archlinux.org/index.php/Direct_Modem_Connection) 這部份設定    
    
<!--more-->  
    
下 `# pppoe-setup` 的時候 跟我說 `command not found `   
    
查了一下才知道要先裝上 `rp-pppoe`    
    
所以要設定之前記得先下    
    
`$ sudo pacman -S rp-pppoe`    
	    
安裝完後再照著上面 ArchWiki 的步驟設定應該就行了    
    
之前不知道要安裝 `rp-pppoe`    
    
結果跑去 ArchWiki 搜尋 `pppoe`    
    
跑出 [Archwiki - pppd](https://wiki.archlinux.org/index.php/pppd) 給我    
    
照著做還是弄不起來 後來才知道要安裝 `rp-pppoe`  
  
所以就是先 `$ sudo pacman -S rp-pppoe` 後   
再 `$ sudo pppoe-setup` 就行了  