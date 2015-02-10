Title: [7zip-cli] [Linux] unzip 7zip file use p7zip
Date: 2013-04-11 18:34
Author: m157q
Category: 7zip
Tags: Linux, 7zip, p7zip
Slug: 7zip-cli-linux-unzip-7zip-file-use-p7zip

組語作業給的 template 是用 7zip 打包成副檔名為 .7z 的檔案    
為了寫 report 想要把 .7z 的 file 解壓縮    
  
<!--more-->  
  
習慣在 CLI 環境下工作    
於是就 google 搜尋了一下有沒有相關的 command    
然後找到了這篇 [http://blog.xuite.net/michaelr/linux/17595860][1]    
    
#關鍵字是 `p7zip`  
    
在 Arch Linux 下    
`$ pacman -Ss p7zip`    
	    
出現以下的訊息    
```  
extra/p7zip 9.20.1-6    
Command-line version of the 7zip compressed file archiver    
```  
  
接著就     
`$ sudo pacman -S p7zip`    
	    
    
安裝完畢之後會多一個 7z 的指令可以使用     
    
想看 man page 的話就     
`$ man 7z`    
我是覺得沒有寫的很清楚啦    
    
所以我又去找了一些網站     
    
底下這個網站有些簡單易懂的範例    
[https://www.ibm.com/developerworks/mydeveloperworks/blogs/6e6f6d1b-95c3-46df-8a26-b7efd8ee4b57/entry/how_to_use_7zip_on_linux_command_line144?lang=en][2]    
    
不過還是沒找到我想要的    
    
如果我直接下    
`$ 7z e xxx.7z`    
就會有悲劇發生  
  
xxx.7z 裏面的東西會全部跟我的當前資料夾所有東西混在一起!!  
所以要怎樣才能讓 7z 在解壓縮一個檔案的時候順便新建一個資料夾把檔案都塞進去呢?    
我 google 到了有人問了同樣的問題(果然不是只有我笨0.0    
[http://superuser.com/questions/95902/7-zip-and-unzipping-from-command-line][3]    
    
結果原來只要    
`$ 7z x xxx.7z`    
	    
沒錯 只要把 e 改成 x 就好了    
    
後來看到其實在 man page 有寫了這些東西    
```  
FUNCTION LETTERS    
	 a Add    
	 d Delete    
	 e Extract    
	 l List    
	 t Test    
	 u Update    
	 x eXtract with full paths    
```  
沒錯 就是最後那行! x!    
    
總之就是這樣 以後解壓縮 .7z 的 file 也跟 .tar .zip 那些檔案一樣    
用 CLI 就可以解決啦    
    
    
  
  
[1]: http://blog.xuite.net/michaelr/linux/17595860  
[2]: https://www.ibm.com/developerworks/mydeveloperworks/blogs/6e6f6d1b-95c3-46df-8a26-b7efd8ee4b57/entry/how_to_use_7zip_on_linux_command_line144?lang=en  
[3]: http://superuser.com/questions/95902/7-zip-and-unzipping-from-command-line  