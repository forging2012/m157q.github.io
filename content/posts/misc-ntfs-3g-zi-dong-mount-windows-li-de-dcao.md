Title: [Misc] ntfs-3g: 自動 mount Windows 裡的 D槽
Date: 2013-02-17 00:32
Author: m157q
Category: Misc
Tags: Misc, Linux, fstab, UUID, Arch, NTFS, ntfs-3g
Slug: misc-ntfs-3g-zi-dong-mount-windows-li-de-dcao

在 Arch 上 mount windows 裏面的D槽    
之前用 Ubuntu 的時候 就一直拿 D 槽當作是共用的存檔地方    
所以灌其他作業系統的時候也不太需要做啥備份    
  
<!--more-->  
  
---  
fstab  
---  
如果要讓 Linux 在開機的時候自動 mount D槽    
    
`$ sudoedit /etc/fstab`    
	    
必須在 `/etc/fstab` 中下寫類似這樣的 rule    
    
```  
# /dev/sda5 (win_D)    
	UUID=01CC0B74E1BC55F0 /win_D ntfs-3g defaults,umask=000  0  2  
```    
  
---     
UUID  
---  
之後使用  `$ lsblk -f` 這個指令去察看要 mount 的硬碟的 UUID    
然後把該 UUID 填寫在 UUID= 的後面    
不知道什麼是 UUID 的可參考[維基百科 UUID][1]     
    
/win_D 是你要把 D 槽 mount 在哪個目錄底下 可以自行修改    
    
---  
ntfs-3g  
---  
    
ntfs-3g 不知道這是什麼的請見[維基百科 NTFS-3G][2]      
    
這裡如果用 ntfs 的話會造成無法寫入和修改權限 所以要用 ntfs-3g    
預設應該是沒安裝的    
在 Arch Linux 請先    
    
`$	sudo pacman -S ntfs-3g`    
	    
defaults,umask=000 0 2 後面這3個部份請參考 [Archwiki-fstab][3] 和 [鳥哥-fstab][4]    
      
需要其他不同的設定的話可以參考後 自行修改options    
  
---  
  
umask用000是因為我這台是個人使用的筆電 為了方便存取D槽才這樣設定    
因為 mount 起來的 owner 和 group 都會是 root    
反正只有我一個人用設777會比較方便 但相對安全性就變低了Orz    
    
    
  
  
[1]: http://zh.wikipedia.org/zh-tw/UUID  
[2]: http://zh.wikipedia.org/zh-tw/NTFS-3G  
[3]: https://wiki.archlinux.org/index.php/Fstab  
[4]: http://linux.vbird.org/linux_basic/0230filesystem.php#fstab  