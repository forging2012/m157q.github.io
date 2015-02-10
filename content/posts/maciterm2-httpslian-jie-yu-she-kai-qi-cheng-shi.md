Title: [Mac][iTerm2] https連結預設開啟程式
Date: 2013-12-10 14:24
Author: m157q
Category: Maciterm2
Tags: mac, Https, iTerm2
Slug: maciterm2-httpslian-jie-yu-she-kai-qi-cheng-shi

iTerm2 會搶走 https 的預設開啟應用程式  
所以每次點 https 連結以後  
就會在 iTerm2 開一個新分頁 然後啥都沒有  
http 連結就不會有這個問題  
  
<!--more-->  
  
google 了好久 終於找到這篇  
[MacUknow - 請問關於https連結預設開啟程式](http://www.macuknow.com/node/20369)  
國外好像都沒人遇到 不然就是我 google skill 太差  
  
---  
  
### 解法  
  
在 terminal 輸入  
  
`open ~/Library/Preferences/com.apple.LaunchServices.plist`  
  
預設會用 Xcode 開啟  
一個個點開檢查 `LSHandlers` 底下的某個 Item  
看到 `LSHandlerURLScheme https` 後  
把底下的 `LSHandlerRoleAll` 改成 `com.google.chrome`  
  
確認修改完之後重新開機  
點選 https 應該就會改回用 Chrome 開啟了  