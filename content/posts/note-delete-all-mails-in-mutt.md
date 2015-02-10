Title: [Note] Delete all mails in Mutt
Date: 2014-08-01 12:37
Author: m157q
Category: Note
Tags: 
Slug: note-delete-all-mails-in-mutt

1. `D` - press **Shift-d** (delete pattern)  
2. `~s .*` then press **enter**. Mutt will flag all mail with a D.  
3. `q` to quit mutt  
  
another way   
  
1. `T` - tag pattern mode  
2. `~s .*` -  tag all mails  
3. `;d` - delete tagged mails  
4. $ (**Shift+4**) - to sync change to your mailbox or `q` to quit mutt  
  
---  
  
### Reference  
  
[Deleting all e-mail messages in your inbox with mutt](http://major.io/2009/06/19/deleting-all-e-mail-messages-in-your-inbox-with-mutt/)  