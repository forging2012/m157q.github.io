Title: Install Arch Linux on MacBook Air 2013-mid
Slug: install-arch-linux-on-macbook-air-2013-mid
Date: 2015-08-19 14:08:04
Authors: m157q
Category: Note
Tags: Arch Linux, MacBook Air, Linux
Summary: 參加完 COSCUP 2015，聽完 jserv 的封麥演說以及一句「Linux 使用者有錢以後就會投入 Mac 的懷抱」覺得自己深深中槍，備感慚愧。於是決定來做一件很久以前其實就想做的事：跟 Linus Torvalds 一樣，把 MacBook Air 上的 OS X 砍了，直接灌 Linux 來用。當然，Arch Linux 是首選。以下紀錄一下過程，給有需要的人參考。

> 警告: 把 OS X 砍掉的話，之後要更新 firmware 必須使用有安裝 OS X 的外接硬碟上開機才能更新。

> 使用上遇到問題，才有動力去解決、改善、貢獻並回饋程式碼到上游。  

改用 OS X 的這兩年，也不是說就完全沒用 Linux 了，舊的筆電退役成 Server 架在宿舍裡，
一個不用桌面環境的 Linux ，使用起來基本上是完全不會遇到太多問題的。
而 OS X 的確遇到使用上的問題減少了。  
用起來的確跟當初想的一樣，是個問題比較沒那麼多的 UNIX-like System  
但同時也在不知不覺中漸漸喪失了解決問題的能力，  
就好像一把兩年前就不再磨的刀劍，愈發鈍鏽。  
當初會買 MacBook Air 而不選擇 UltraBook 的原因主要是因為價錢、續航力、重量都是 MacBook Air 勝出，  
當然之後在使用上，我也對重量和續航力很滿意，
但其實在使用 OS X 上也遇過許多無法接受的問題，有些妥協了，有些沒有  
例如：
+ 原生的工具都非常老舊，舊版本代表著很多問題，無論是資安或是有無新功能。這對於一個從使用 Rolling Release 的 Arch Linux user 來說真的很不習慣。    
    + 骨灰級的 Bash 真的令我印象深刻，如果沒有 Homebrew 的話，我肯定無法用這麼久，感謝 @mxcl
+ 接網路線跟螢幕線得額外花錢買轉接頭
    + 兩個加起來新台幣 1,600 左右。恩，我跟很多人一樣都買了。
+ OS X 10.9 以前的視窗放大真的很雞肋和令人哭笑不得，放大後不會佔滿整個桌面，有時候甚至比按完放大前更小。 
    + 在 OS X 10.10 後，放大功能只接改成全螢幕了
+ 雙螢幕在 OS X 10.10 仍然有一個我常常踩到的詭異Bug，如果有程式被丟到外接螢幕那邊，在不拔掉螢幕線的情況下，把螢幕闔上進入休眠，接著把螢幕線拔掉，然後喚醒 Mac，這時候就會發現被丟到外接螢幕的應用程式仍然被認為是在外接螢幕的範圍，但因為早就沒有外接螢幕了，所以即便程式仍然在執行，使用者也根本看不到畫面，重點是重新執行該程式也無法解決這問題，只能登出、重開機或是重新接上外接螢幕在電腦喚醒的情況下拔掉螢幕線，或是把該程式拉回原生螢幕，才有辦法解決。
+ 系統介面內建中文字型很難看，要改也很難改。
    + OS X 10.9 以前有 TCFail 能用，到了 OS X 10.10 只能去改系統檔案設定，而換成了我想用的字型以後，內建的中文輸入法就會掛掉，只好又改回原本的字型。
+ 輸入法也是個問題
    + 剛用 OS X 10.8 的時候就聽很多人說內建的中文輸入法爛爛的，沒有智慧選詞、不能自建詞庫之類的，所以很多人都裝小麥或者是開源的香草，但我用了以後還是不太習慣。後來找到另一款開源的中州韻輸入法(RIME)，是對岸的中國人[佛振](https://github.com/lotem)開發的，在 Windows, Linux, Mac 上都能使用。裝來用以後發現還不錯用，自訂性蠻強大的，由於在用 gcin 時，我習慣把選字鍵從常人慣用的 1234567890 改成 asdfghjkl; 以減少手指移動的距離，這款輸入法也能做到，於是就用了。(至於後來關於 dvorak 跟拼音輸入法又是另一個故事了)
    + 到了 OS X 10.10 之後，不知怎的，非官方的中文輸入法都變得超級慢，慢到無法接受，於是又換回不是很好用的官方中文輸入法。

一不小心好像離題寫了太多關於 OS X 的部份。  
Anyway, 因為種種問題加上這次 COSCUP 的助力，促使我把 Arch Linux 灌在 Mac 上，以下是紀錄。


---
# Install Arch Linux Only (No OS X Dual Boot) on MacBook Air
> WARNING: After erasing OS X, We can only update the MacBook Air firmware via the external drive which has already installed OS X.

1. Make Arch Linux bootable Live USB
    + Go to <> and download the newest Arch Linux iso.
    + Plug in a USB drive
    + use `diskutil list` to find the USB dirve `/dev/sdX`
    + `dd if=$(path to arch linux iso) of=/dev/rsdX bs=1m`
        + use raw disk (/dev/rsdX) make this quicker. 
2. Go to AppStore for updating OS X to the newest version
    + After the first update, reboot, and check for newest update again
    + Make sure it's newest update, espcially the firmware udpate
3. Erase OS X
    + Reboot MacBook Air
    + Press Command + R to enter the Reinstall mode 
    + Choose DiskUtility and Erase the entire disk
4. Entering Arch Linux Live USB installation
    + Reboot MacBook Air
    + Press alt/option key for entering EFI bootloader
    + Choose EFI USB
5. Install Arch Linux (Just like the normal installation)
    + `cgdisk /dev/sda`

# Desktop Environment
## configs
Download my own config files on <https://github.com/M157q/rcfiles>

`git clone https://github.com/M157q/rcfiles`
`cd rcfiles`
`make install`

## Synaptic
`sudo pacman -S xf86-input-synaptics`   #for touchpad

## Sound
`sudo pacman -S xf86-video-intel`
`sudo pacman -S alsa-utils` #for alsamixer, amixer

## awesomewm
`sudo pacman -S awesome`
`sudo pacman -S vicious`    #for rc.lua

## Chinese
`sudo pacman -S gcin`       #Chinese IME

## Browser
`sudo pacman -S firefox`

## Fonts

# Misc
## Python 
`sudo pacman -S python2 python-pip`
`sudo pip install virtualenvwrapper`


---

# References
+ <https://github.com/pandeiro/arch-on-air> 
    + Dual Boot
+ <https://wiki.archlinux.org/index.php/MacBook> 
    + Arch Linux Only, Dual Boot, Arch Linux + OS X + Windows
