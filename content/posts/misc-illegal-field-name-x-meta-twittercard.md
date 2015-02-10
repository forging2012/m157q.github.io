Title: [Misc] Illegal field name 'X-Meta-Twitter:card'
Date: 2013-05-08 07:44
Author: m157q
Category: Misc
Tags: Misc, perl, CPAN, WWW::Mechanize, X-Meta-Twitter:card
Slug: misc-illegal-field-name-x-meta-twittercard

最近因為 NA 作業2 開始寫 Perl    
其中一個是寫 IRC bot    
作業 Demo 完後自己繼續開發新功能    
要做檢查到 URL 就回應該 URL Html source 的 title label 和 縮網址    
用了 CPAN 的 WWW::Mechanize    
結果 xatier 丟了 [https://gist.github.com/xatier/5538258][1] 出來後    
IRC bot 就 die 了    
噴出了這行錯誤    
`Illegal field name 'X-Meta-Twitter:card' at .../HTML/HeadParser.pm line 207.`    
    
<!--more-->    
    
    
Google 了一下 Error Message 發現不少人都有遇到    
[http://s1737.socode.us/question/515025cfe8432c042628864f][2]    
    
根據這篇底下的 comment 找到了答案 (其實自己先 Trace code 之後也找到了同樣的地方    
[https://github.com/libwww-perl/http-message/issues/3#issuecomment-10118644][3]    
    
問題就出在 `perl5/lib/per5/HTTP/Headers.pm`    
(`HTML::HeadParser` 有用到 `HTTP::Headers`    
    
裏面有個叫 `_header` 的 subroutine (不過在上面那篇的 comment 裏面好像是 header    
    
裏面有一行  
```perl  
Carp::croak("Illegal field name '$field'") if rindex($field, ':') > 1 || !length($field);  
```  
問題就出在   
```perl  
rindex($field, ':') > 1  
```    
  
只要 : 後面有東西的話就會回傳 True    
    
Twiiter:card 的 : 後面有 card 所以被判定成 Illegal field name 了    
    
要修正的話就照那個 comment 說的    
    
把該行改成    
```perl  
Carp::croak("Illegal field name '$field'") if $field !~ /^X-Meta/ && rindex($field, ':') > 1 || !length($field);  
```  
    
這樣就不會判斷 X-Meta 開頭的了    
    
只是這問題己經 6~7 個月了 開發者最近 commit 的時間也還是 2 個月前    
    
不懂為啥這問題遲遲不解決@@  
  
[1]: https://gist.github.com/xatier/5538258  
[2]: http://s1737.socode.us/question/515025cfe8432c042628864f  
[3]: https://github.com/libwww-perl/http-message/issues/3#issuecomment-10118644  