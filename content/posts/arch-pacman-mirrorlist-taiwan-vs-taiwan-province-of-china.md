Title: [Arch] pacman mirrorlist - Taiwan vs. Taiwan (Province of China)
Date: 2014-10-29 20:53
Author: m157q
Category: Arch
Tags: taiwan, Archlinux, pacman, mirrorlist
Slug: arch-pacman-mirrorlist-taiwan-vs-taiwan-province-of-china

這是個有點久以前的故事了  
[2012/06/26 的 pacman mirrorlist commit](https://projects.archlinux.org/svntogit/packages.git/commit/trunk?h=packages/pacman-mirrorlist&id=4ebeb6161b4f178b9f3105d47a2c408bc1dd9547)  
把 Taiwan 改成了 Taiwan (Province of China)  
然後就有台灣人在 Arch Bugs Report 發起一則 Bug Report  
[FS#30444 - Download Page uses Taiwan's name as “Taiwan, Province of China”](https://bugs.archlinux.org/task/30444)  
要求把名字改回 Taiwan  
  
<!--more-->  
  
陸陸續續也有人去發 Bug Report 要求正名  
+ [FS#35586 - Please change "Taiwan, province of china" to "Taiwan in pacman-mirrorlist](https://bugs.archlinux.org/task/35586)  
+ [FS#35757 - Listing for Taiwan](https://bugs.archlinux.org/task/35757)  
+ [FS#37973 - Taiwan is not a province of China...](https://bugs.archlinux.org/task/37973)  
  
然後之後就被 Admin 拿 [ISO 3166](http://en.wikipedia.org/wiki/ISO_3166) 打槍  
![Screen Shot 2014-10-30 at 4.19.38 AM.png](http://user-image.logdown.io/user/5428/blog/5443/post/240404/dlQAhDmWQseNhbwQelis_Screen%20Shot%202014-10-30%20at%204.19.38%20AM.png)  
把相關所有 Report 都 close 掉  
  
直到剛剛  
下個 `sudo pacman -Syu` 更新 Arch，再用 `sudo pacdiff` 更新設定檔的時候  
發現從 Taiwan (Province of China) 改回 Taiwan 了  
![Screen Shot 2014-10-30 at 3.38.24 AM.png](http://user-image.logdown.io/user/5428/blog/5443/post/240404/X5u54zGR4aZRcoe4zp5A_Screen%20Shot%202014-10-30%20at%203.38.24%20AM.png)  
覺得有點訝異和好奇  
查了下官網也沒啥相關公告  
然後去翻了一下[最新的 commit log](https://projects.archlinux.org/svntogit/packages.git/commit/?h=packages/pacman-mirrorlist&id=6438bca958924f781d166c2a473abecd3db54670)  
和舊的比較一下  
發現是同一個 committer  
![Screen Shot 2014-10-30 at 4.41.21 AM copy.png](http://user-image.logdown.io/user/5428/blog/5443/post/240404/RaXDvPn7SvaNRmvpBIdm_Screen%20Shot%202014-10-30%20at%204.41.21%20AM%20copy.png)  
再去看了一下 [Arch Linux 官網的 Download Page](https://www.archlinux.org/download/)  
台灣的部分還真的改回來變成 Taiwan 了  
![Screen Shot 2014-10-30 at 4.06.12 AM.png](http://user-image.logdown.io/user/5428/blog/5443/post/240404/lZMcvLDQTK8djSrorlJC_Screen%20Shot%202014-10-30%20at%204.06.12%20AM.png)  
於是又去找了一下 [Google Cache](http://webcache.googleusercontent.com/search?q=cache:nsRN9P-SvTgJ:https://www.archlinux.org/download/+&cd=1&hl=en&ct=clnk&gl=tw) 確認一下是不是最近發生的事  
發現還是舊的 Taiwan (Province of China)  
![Screen Shot 2014-10-30 at 4.50.57 AM.png](http://user-image.logdown.io/user/5428/blog/5443/post/240404/Vx0iEmEwRGSF4xwPWObE_Screen%20Shot%202014-10-30%20at%204.50.57%20AM.png)  
所以就確定是最近發生的事了  
  
不過我不太清楚改回來的原因是啥  
（其實我也不知道當初被從 Taiwan 改成 Taiwan (Province of China) 的原因）  
發個[噗浪狀態](http://www.plurk.com/p/ki0evh)後就有人跑去要求 [re-open](https://bugs.archlinux.org/task/30444#actionbuttons) 了 囧  
>> 2014-10-29: A request to re-open the task has been made. Reason for request: ISO claimed that the country name is not part of the ISO 3166 standard, thus it's still a WONTFIX for the upstream, ArchLinux is responsible for the issue for regarding something not-in-fact-in-a-standard as standard, thus request re-open. Falling back to the complex procedure of finding country names *least* irritating for everyone is both sane and required.  
  
![Screen Shot 2014-10-30 at 4.54.26 AM.png](http://user-image.logdown.io/user/5428/blog/5443/post/240404/nqx4HcIQPGmvAxgEKNQp_Screen%20Shot%202014-10-30%20at%204.54.26%20AM.png)  
  
且看這次會如何回應吧?  
  
# Reference  
+ <http://planykao.blogspot.tw/2012/07/taiwan-is-not-province-of-china.html>  