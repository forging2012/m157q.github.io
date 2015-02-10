Title: [VIM] wrong % (matching parens searching) action
Date: 2014-08-12 20:27
Author: m157q
Category: Vim
Tags: Vim
Slug: vim-wrong-matching-parens-searching-action

cpoptions in VIM are so complicated...  
  
`{'{,''}’}` this pattern will cause a wrong % action (MATCHING PARENTHESES SEARCH) in VIM with default cpoptions flag.  
  
[Here's a real Example in JavaScript](pastebin.com/bEHix2hD)  
  
And if we `:set cpoptions&vi` to change cpoptions let VIM act like VI, the result seems correct.  
  
But after read the doc in VIM, proved it was a coincidence because VI just treat this pattern a PLAINTEXT without considering parens in “” or ''. So, if you remove one of the parens, the result get wrong again.  
  
What I am curious about is that the default syntax highlighting is correct but the % action is wrong in VIM with such pattern.  
  
I know install a plugin like matchit can probably resolve this problem. But is there any built-in method to deal with it?  
  
My friend found this problem while he was trying to fold his code and got an unpredictable result.  
  
  
### References  
+ [Vim finds incorrect matching bracket when using %](http://stackoverflow.com/questions/1903225/vim-finds-incorrect-matching-bracket-when-using)  